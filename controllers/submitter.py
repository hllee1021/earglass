import os
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, redirect, request, make_response, flash
import services
from settings import UPLOAD_DIR

controller = Blueprint("submitter", __name__)


@controller.route("/", methods=["GET"])
def get_submitter_home():
    id = int(request.cookies.get("id"))
    tasks = services.submitter.tasklist_detail(id)
    tasks = list(zip(range(1, len(tasks)+1), tasks))
    print(tasks)
    return render_template("submitter/submitter_home.html", tasks=tasks)


@controller.route("/agreement", methods=["GET"])
def agreement():
    task_id = request.args.get('task_id', 0)
    print(task_id)
    return render_template("submitter/agreement.html", task_id = task_id)


@controller.route("/agree", methods=["POST"])
def submitter_home():
    agree = request.form.get("agree")
    task_id = request.form.get("task_id")
    print(agree)
    if agree == "agree":
        # agreement processing code
        flash("테스크 참여 신청되었습니다.")

        # db 쿼리문

        return redirect("/")
    else:
        flash("개인정보 활용에 동의하셔야 테스크에 참여가 가능합니다.")
        return redirect("/")

@controller.route("/my_task", methods=["GET"])
def get_my_task_submitter():
    id = int(request.cookies.get("id"))
    tasks = services.submitter.participating_tasklist(id)
    tasks = list(zip(range(1, len(tasks)+1), tasks))
    
    return render_template("submitter/my_task.html", tasks=tasks)


@controller.route("/submit_task", methods=["POST"])
def submit_task():
    # new task processing code
    file = request.files['file']
    fname = secure_filename(file.filename)
    path = os.path.join(UPLOAD_DIR + "/odsf/", fname)
    file.save(path)
    flash("제출이 완료되었습니다. ㅅㅂ~ 그만 집에 보내줘...")

    return redirect("/")