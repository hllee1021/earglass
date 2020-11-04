from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("users", __name__)


@controller.route("/login", methods=["POST"])
def post_login_data():
    user_id = request.form.get("username")
    password = request.form.get("password")
    print(user_id)
    print(password)

    # 로그인 성공
    if users.verify_user(user_id, password):
        # not "/my", "my". "my" == "/users/my", "/my" = "/my"
        res = make_response(redirect("my"))
        res.set_cookie("user_id", user_id)
        return res
    else:
        flash("로그인 실패. 다시 시도하세요")
        return redirect("/")


@controller.route("/logout", methods=["GET"])
def logout():
    res = make_response(redirect("/"))
    res.delete_cookie("user")
    return res


@controller.route("/my", methods=['GET'])
def mypage():
    # 쿠키가 있다 -> 로그인된 유저라면
    user_id = request.cookies.get("user_id")
    print('user_id:', user_id)
    user = users.get_user_by_id(user_id)
    if user:  # 로그인 된 경우
        return render_template("my.html", user=user)
    else:
        flash("로그인되지 않았습니다")
        return redirect("/")
