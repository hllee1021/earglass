from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import task

controller = Blueprint("task", __name__)

@controller.route("/detail", methods=["GET"])
def Taskdetail():
    return render_template("task_detail.html")

@controller.route("/agree", methods=["POST"])
def submitter_home():
    agree = request.form.get("agree")
    # agreement processing code
    return redirect("submitter_home")

@controller.route("/submit_page", methods=["GET"])
def submit_page():
    return render_template("submit_page.html")

@controller.route("/submit_task", methods=["POST"])
def submit_task():
    # new task processing code
    return redirect("submitter_home")