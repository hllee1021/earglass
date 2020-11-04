from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import admin

# writed by seungsu

controller = Blueprint("controller", __name__)


@controller.route("/", methods=["GET"])
def get_main_admin():
    return render_template()


@controller.route("/submitter/<int:user_id>", methods=["GET"])
def get_detail_submitter(user_id):
    return render_template()


@controller.route("/estimator/<int:user_id>", methods=["GET"])
def get_detail_estimator(user_id):
    return render_template()


@controller.route("/task", methods=["POST"])
def add_task():
    return render_template()

@controller.route("/task", methods=["PUT"])
def modify_task():
    return render_template()



@controller.route("/task/<int:task_id>", methods=["GET"])
def detail_task(task_id):
    # show task detail
    return render_template()
