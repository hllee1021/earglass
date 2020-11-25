from flask import Blueprint, render_template, redirect, request, make_response, flash
import services
from database.connection import queryall, queryone

# writed by seungsu

controller = Blueprint("admin", __name__)



@controller.route("/", methods=["GET"])
def admin_home():
    tasks = services.admin.get_all_tasks()
    submitters = queryall("SELECT * FROM USER WHERE FK_UserTypeName = '제출자'")
    for user in submitters:
        user_id = user['idUSER']
        tasks = queryall("SELECT FK_TaskName FROM PARTICIPATION WHERE FK_idUSER=%s AND Status = 'ongoing'", (user_id, ))
        user['Tasks'] = tasks

    estimators = queryall("SELECT * FROM USER WHERE FK_UserTypeName = '평가자'")
    for user in estimators:
        user_id = user['idUSER']
        tasks = queryall("SELECT P.TaskName FROM EVALUATION AS E  \
            LEFT JOIN PARSING_DSF AS P ON E.FK_idPARSING_DSF = P.idPARSING_DSF WHERE E.FK_idEstimator=%s AND E.Status = 'ongoing' " , (user_id, ))
        user['Tasks'] = tasks

    users = submitters + estimators
    return render_template("admin/admin.html", tasks=tasks, users=users)

@controller.route("/add_task", methods=["GET"])
def get_add_task_page():
    return render_template("admin/add_task.html")

@controller.route("/adding_task", methods=["POST"])
def get_adding_task_page():
    return render_template("admin/add_task.html")

@controller.route("/edit_task", methods=["GET"])
def get_edit_task_page():
    return render_template("admin/edit_task.html")

@controller.route("/task_info", methods=["GET"])
def get_task_page():
    return render_template("admin/task_info.html")

<<<<<<< HEAD
@controller.route("/submitter/<submitter_id>", methods=["GET"])
def get_admin_submitter_page(submitter_id):
    user = services.users.get_user_by_id(submitter_id)
    participation = services.submitter.participating_tasklist(submitter_id)
=======
@controller.route("/task_info", methods=["GET"])
def get_task_info_page():
    return render_template("admin/task_info.html")

@controller.route("/submitter/<submitter_index>", methods=["GET"])
def get_admin_submitter_page(submitter_index):
    user = services.users.get_user_by_index(submitter_index)
    participation = services.submitter.participating_tasklist(submitter_index)
>>>>>>> 69aa75d4667b31c5a9f07653b6b1e9caaf8ebd47
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

