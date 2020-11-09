from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("estimator", __name__)


@controller.route("/", methods=["GET"])
def get_estimator_home():
    return render_template("estimator/estimator_home.html")