from flask import Blueprint, render_template, redirect, request, make_response, flash
from services import users

controller = Blueprint("estimator", __name__)


@controller.route("/", methods=["GET"])
def get_estimator_home():
    tasks = [{"id": 1, "name":"aa","submitter_name":"hllee1021", "deadline":"1234"},{"id": 2, "name":"bb", "submitter_name":"seungsu","deadline":"1234"},{"id": 3, "name":"cc","submitter_name":"귀요미","deadline":"1234"}]
    return render_template("estimator/estimator_home.html", tasks=tasks)


@controller.route("/pdsf_detail", methods=["GET"])
def get_pdsf_detail():
    tasks = [{"id": 1, "name":"aa","submitter_name":"hllee1021", "score":"100", "pass":"P","date":"2020/11/20"},{"id": 2, "name":"bbb","submitter_name":"1231asf", "score":"50", "pass":"N","date":"2020/12/20"},{"id": 3, "name":"lala","submitter_name":"qwe123123", "score":"70", "pass":"P","date":"2020/9/20"}]
    return render_template("estimator/pdsf_detail.html",tasks=tasks)

#made by 학림
@controller.route("/estimator_task_info", methods=["GET"])
def get_estimator_task_info():
    tasks = {"name":"im_task","description":"card data please~~ samsung good good", "schema_info":"스키마 인포 어떻게 쓰지이", "deadline":"2020/11/20","pass_cut":"중복 튜플 수에 대해서 널널하게 해도 되니까, null 비율에 엄격하게 해주세용"}
    return render_template("/estimator/estimator_task_info.html",tasks=tasks)