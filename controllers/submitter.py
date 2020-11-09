from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("submitter", __name__)


@controller.route("/", methods=["GET"])
def get_submitter_home():
    return render_template("submitter_home.html")