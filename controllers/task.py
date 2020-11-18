from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import task

controller = Blueprint("task", __name__)

@controller.route("/detail", methods=["GET"])
def task_detail():
    task_id = request.args.get('id', 0)

    # db 테스크 정보를 주세요
    print(task_id)
    opt = "info"
    task={}
    test = [{"id": 1, "name":"aa", "deadline":"1234"},{"id": 2, "name":"bb", "deadline":"1234"},{"id": 3, "name":"cc", "deadline":"1234"}]
    data_type=["csv","smi","scv"]
    return render_template("task/task_detail.html", opt=opt, task=task, test=test, data_type=data_type)

@controller.route("/detail", methods=["POST"])
def task_detail_post():
    opt = request.form.get("opt", "info")
    return render_template("task/task_detail.html", opt=opt)