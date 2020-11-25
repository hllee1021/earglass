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
    leaderboard = list(zip(range(1, len(leaderboard)+1), leaderboard))

    my_submit = services.submitter.my_submission_list(task_id, user_pk)
    my_submit = list(zip(range(1, len(my_submit)+1), my_submit))

    odsf_type = services.submitter.all_origin_data_type(task_id);
    return render_template("task/task_detail.html", opt=tab, task_info=task_info, leaderboard=leaderboard, my_submit=my_submit, odsf_type=odsf_type)
