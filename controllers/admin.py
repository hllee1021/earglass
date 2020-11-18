from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import admin
from database.connection import queryall, queryone

# writed by seungsu

controller = Blueprint("admin", __name__)



# @controller.route("/submitter/<int:user_id>", methods=["GET"])
# def get_detail_submitter(user_id):
#     pass


# @controller.route("/estimator/<int:user_id>", methods=["GET"])
# def get_detail_estimator(user_id):
#     pass


# @controller.route("/task", methods=["POST"])
# def add_task():
#     pass


# @controller.route("/task", methods=["PUT"])
# def modify_task():
#     pass


# @controller.route("/task/<int:task_id>", methods=["GET"])
# def detail_task(task_id):
#     # show task detail
#     pass


@controller.route("/", methods=["GET"])
def admin_home():
    tasks = queryall("""
SELECT TASK.*,
(SELECT COUNT(TaskName) FROM PARSING_DSF WHERE PARSING_DSF.TaskName=TASK.TaskName) as ParsingDsfCount,
(SELECT COUNT(TaskName) FROM PARSING_DSF WHERE PARSING_DSF.Pass='P' AND PARSING_DSF.TaskName=TASK.TaskName) as PassedParsingDsfCount
FROM TASK
""")
    users = queryall("SELECT * FROM USER")
    return render_template("admin/admin.html", tasks=tasks, users=users)

@controller.route("/add_task", methods=["GET"])
def get_add_task_page():
    return render_template("admin/add_task.html")

@controller.route("/task", methods=["GET"])
def get_task_page():
    return render_template("admin/task.html")

@controller.route("/task_info", methods=["GET"])
def get_task_info_page():
    return render_template("admin/task_info.html")
