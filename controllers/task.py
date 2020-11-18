from flask import Blueprint, render_template, redirect, request, make_response, flash
import services

controller = Blueprint("task", __name__)

@controller.route("/detail", methods=["GET"])
def task_detail():
    user_pk = int(request.cookies.get("id"))
    task_id = request.args.get('task_id', 0)
    tab = request.args.get('tab', 'info')

    # db 테스크 정보를 주세요
    task_info = services.submitter.task_info(task_id)
    leaderboard = services.submitter.leaderboard(task_id)
    my_submit = services.submitter.my_submission_list(task_name, user_pk)
    
    data_type=["csv","smi","scv"]
    return render_template("task/task_detail.html", opt=tab, task_info=task_info, leaderboard=leaderboard, my_submit=my_submit)