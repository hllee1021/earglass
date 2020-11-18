from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("estimator", __name__)


@controller.route("/", methods=["GET"])
def get_estimator_home():
    tasks = [{"id": 1, "name":"aa","submitter_name":"hllee1021", "deadline":"1234"},{"id": 2, "name":"bb", "submitter_name":"seungsu","deadline":"1234"},{"id": 3, "name":"cc","submitter_name":"귀요미","deadline":"1234"}]
    return render_template("estimator/estimator_home.html", tasks=tasks)


@controller.route("/pdsf_detail", methods=["GET"])
def get_pdsf_detail():
    return render_template("estimator/pdsf_detail.html")
