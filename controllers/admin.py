from flask import Blueprint, render_template, redirect, request, make_response, flash
import services
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
    tasks = services.admin.get_all_tasks()
    submitters = queryall("SELECT * FROM USERS WHERE FK_UserTypeName = \'제출자\'")
    for user in submitters:
        user_id = user['idUSER']
        tasks = queryall("SELECT FK_TaskName FROM PARTICIPATION WHERE FK_idUSER=%s AND Status = \'ongoing\'", (user_id, ))
        user['Tasks'] = tasks

    estimators = queryall("SELECT * FROM USERS WHERE FK_UserTypeName = \'평가자\'")
    for user in estimators:
        user_id = user['idUSER']
        tasks = queryall("SELECT P.FK_TaskName FROM EVALUATION AS E  \
            LEFT JOIN PARSING_DSF AS P ON E.FK_idPASRSING_DSF = P.idPARSING_DSF WHERE E.FK_idEstimator=%s AND E.Status = \'ongoing\' " , (user_id, ))
        user['Tasks'] = tasks

    users = submitters + estimators
    
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
