from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("submitter", __name__)


@controller.route("/", methods=["GET"])
def get_submitter_home():
    return render_template("submitter/submitter_home.html")


@controller.route("/agree", methods=["POST"])
def submitter_home():
    agree = request.form.get("agree")
    # agreement processing code
    return redirect("submitter/agreement.html")


@controller.route("/submit_page", methods=["GET"])
def submit_page():
    return render_template("submitter/submit_page.html")


@controller.route("/submit_task", methods=["POST"])
def submit_task():
    # new task processing code
    return redirect("submitter/submitter_home")