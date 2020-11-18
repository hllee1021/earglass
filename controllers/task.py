from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import task

controller = Blueprint("task", __name__)

@controller.route("/detail", methods=["GET"])
def task_detail():
    task_id = request.args.get('id', 0)

    # db 테스크 정보를 주세요
    
    print(task_id)
    opt = "info"
    return render_template("task/task_detail.html", opt=opt, task_id=task_id)

@controller.route("/detail", methods=["POST"])
def task_detail_post():
    opt = request.form.get("opt", "info")
    return render_template("task/task_detail.html", opt=opt)