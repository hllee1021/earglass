from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import task

controller = Blueprint("task", __name__)

@controller.route("/detail", methods=["GET"])
def Taskdetail():
    return render_template("task/task_detail.html")

