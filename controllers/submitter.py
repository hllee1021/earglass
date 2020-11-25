import os
from io import StringIO
import json
import pandas as pd
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, redirect, request, make_response, flash, Response
import services
from settings import UPLOAD_DIR

controller = Blueprint("submitter", __name__)


@controller.route("/", methods=["GET"])
def get_submitter_home():
    id = int(request.cookies.get("id"))
    tasks = services.submitter.tasklist_detail(id)
    tasks = list(zip(range(1, len(tasks)+1), tasks))
    print(tasks)
    return render_template("submitter/submitter_home.html", tasks=tasks)


@controller.route("/agreement", methods=["GET"])
def agreement():
    task_id = request.args.get('task_id', 0)
    print(task_id)
    return render_template("submitter/agreement.html", task_id = task_id)


@controller.route("/agree", methods=["POST"])
def submitter_home():
    agree = request.form.get("agree")
    task_id = request.form.get("task_id")
    print(agree)
    if agree == "agree":
        # agreement processing code
        flash("테스크 참여 신청되었습니다.")

        # db 쿼리문

        return redirect("/")
    else:
        flash("개인정보 활용에 동의하셔야 테스크에 참여가 가능합니다.")
        return redirect("/")

@controller.route("/my_task", methods=["GET"])
def get_my_task_submitter():
    id = int(request.cookies.get("id"))
    tasks = services.submitter.participating_tasklist(id)
    tasks = list(zip(range(1, len(tasks)+1), tasks))
    
    return render_template("submitter/my_task.html", tasks=tasks)


@controller.route("/submit_task", methods=["POST"])
def submit_task():
    # new task processing code
    file = request.files['file']
    fname = secure_filename(file.filename)
    path = os.path.join(UPLOAD_DIR + "/odsf/", fname)
    file.save(path)
    flash("제출이 완료되었습니다. ㅅㄱ~ 그만 집에 보내줘...")

    return redirect("/")

# , method=["POST"]
@controller.route("/task/download")
def csv_file_download_with_stream():

    odsf_type_id = int(request.args.get('odsf_type_id', 0))

    if odsf_type_id != 0:
        odsf_type = services.submitter.odsf_type_schema_info(odsf_type_id)
    else:
        return redirect("/my_task")

    filename = f"{odsf_type['TaskName']}_{odsf_type['DataTypeName']}"

    # schema에 맞는 df 생성
    schema = json.loads(odsf_type['MappingInfo'])
    schema = list(schema.keys())
    temp_df = pd.DataFrame(columns=schema)

    # dataframe을 저장할 IO stream 
    output_stream = StringIO()

    # 그 결과를 앞서 만든 IO stream에 저장
    temp_df.to_csv(output_stream)
    response = Response(
        output_stream.getvalue(), 
        mimetype='text/csv', 
        content_type='application/octet-stream',
    )

    response.headers["Content-Disposition"] = f"attachment; filename={filename}.csv"

    return response 