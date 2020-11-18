from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import task

controller = Blueprint("task", __name__)

@controller.route("/detail", methods=["GET"])
def task_detail():
    opt = "info"
    return render_template("task/task_detail.html", opt=opt)

@controller.route("/detail", methods=["POST"])
def task_detail_post():
    opt = request.form.get("opt", "info")
    return render_template("task/task_detail.html", opt=opt)