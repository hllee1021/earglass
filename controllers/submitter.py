from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("submitter", __name__)


@controller.route("/", methods=["GET"])
def get_submitter_home():
    return render_template("submitter/submitter_home.html")


@controller.route("/agreement", methods=["GET"])
def agreement():
    return render_template("submitter/agreement.html")


@controller.route("/agree", methods=["POST"])
def submitter_home():
    agree = request.form.get("agree")
    print(agree)
    if agree == "agree":
        # agreement processing code
        flash("테스크 참여 신청되었습니다.")
        return redirect("/")
    else:
        flash("개인정보 활용에 동의하셔야 테스크에 참여가 가능합니다.")
        return redirect("/")

@controller.route("/my_task", methods=["GET"])
def get_my_task_submitter():
    return render_template("submitter/my_task.html")


@controller.route("/submit_task", methods=["POST"])
def submit_task():
    # new task processing code
    flash("제출되었습니다.")
    return redirect("/")