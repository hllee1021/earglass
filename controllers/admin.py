from flask import Blueprint, render_template, redirect, request, make_response, flash
import services
from database.connection import queryall, queryone

# writed by seungsu

controller = Blueprint("admin", __name__)



@controller.route("/", methods=["GET"])
def admin_home():
    tasks = services.admin.get_all_tasks()

    # 제출자들이 참여하는 태스크 목록
    submitters = queryall("SELECT * FROM USER WHERE FK_UserTypeName = '제출자'")
    for submitter in submitters:
        user_index = submitter['idUSER']
        participating_tasks = queryall("SELECT FK_TaskName FROM PARTICIPATION WHERE FK_idUSER=%s AND Status = 'ongoing'", (user_index, ))
        submitter['Tasks'] = participating_tasks

    # 평가자들이 참여하는 태스크 목록
    estimators = queryall("SELECT * FROM USER WHERE FK_UserTypeName = '평가자'")
    for estimator in estimators:
        user_index = estimator['idUSER']
        participating_tasks = queryall("SELECT P.TaskName FROM EVALUATION AS E  \
            LEFT JOIN PARSING_DSF AS P ON E.FK_idPARSING_DSF = P.idPARSING_DSF WHERE E.FK_idEstimator=%s AND E.Status = 'ongoing' " , (user_index, ))
        estimator['Tasks'] = participating_tasks

    users = submitters + estimators
    return render_template("admin/admin.html", users=users, tasks=tasks)

@controller.route("/add_task", methods=["GET"])
def get_add_task_page():
    return render_template("admin/add_task.html")

@controller.route("/add_task", methods=["POST"])
def get_adding_task_page():
    return render_template("admin/add_task.html")

@controller.route("/edit_task", methods=["GET"])
def get_edit_task_page():
    return render_template("admin/edit_task.html")

@controller.route("/task_info/<task_name>", methods=["GET"])
def get_task_page(task_name):
    task = services.admin.task_info(task_name)
    origin_data_types = services.admin.task_info_origin_data_type(task_name)
    print(origin_data_types)
    return render_template("admin/task_info.html", task=task, origin_data_types=origin_data_types)

@controller.route("/submitter/<submitter_index>", methods=["GET"])
def get_admin_submitter_page(submitter_index):
    user = services.users.get_user_by_index(submitter_index)
    participation = services.submitter.participating_tasklist(submitter_index)
    if not user:
        flash("해당 id에 대한 유저가 존재하지 않습니다")
        return redirect("/admin/")

    return render_template("admin/submitter.html", user=user, participation=participation)

@controller.route("/estimator", methods=["GET"])
def get_admin_estimator_page():
    return render_template("admin/estimator.html")

@controller.route("/my", methods=["GET"])
def get_admin_my_page():
    return render_template("admin/my.html")

