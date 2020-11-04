from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("controller", __name__)


@controller.route("/login", methods=["GET"])
def get_login_page():
    return render_template('login.html')


@controller.route("/login", methods=["POST"])
def post_login_data():
    username = request.form.get("username")
    password = request.form.get("password")

    # 로그인 성공
    if users.verify_user(username, password):
        # not "/my", "my". "my" == "/users/my", "/my" = "/my"
        res = make_response(redirect('my'))
        res.set_cookie("user", username)
        flash("성공적으로 로그인되었습니다")
        return res

    # 로그인 실패
    else:
        flash("로그인에 실패하였습니다")
        return redirect('my')


@controller.route("/my", methods=["GET"])
def get_my_page():
    username = request.cookies.get("user")
    user = users.get_user_by_id(username)
    if user:
        return render_template("my.html", user=user)
    else:
        return redirect("login")


@controller.route("/logout", methods=["GET"])
def logout():
    res = make_response(redirect('login'))
    res.delete_cookie('user')
    return res


@controller.route("/test", methods=["GET"])
def test():
    return render_template('sign_up.html')