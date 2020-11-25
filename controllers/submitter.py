import os
from io import StringIO
import json
import pandas as pd
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, redirect, request, make_response, flash, Response
import services
import system_estimator
from settings import UPLOAD_DIR

controller = Blueprint("submitter", __name__)


@controller.route("/", methods=["GET"])
def get_submitter_home():
    user_index = int(request.cookies.get("user_index"))
    tasks = services.submitter.tasklist_detail(user_index)
    print(tasks)
    return render_template("submitter/submitter_home.html", tasks=tasks)


@controller.route("/agreement", methods=["GET"])
def agreement():
    task_name = request.args.get('task_name', 0)
    print(task_name)
    return render_template("submitter/agreement.html", task_name = task_name)


@controller.route("/agree", methods=["POST"])
def submitter_home():
    agree = request.form.get("agree")
    task_name = request.form.get("task_name")
    user_index = request.cookies.get("user_index")
    print(agree)
    if agree == "agree":
        # agreement processing code
        services.submitter.insert_participation(task_name, user_index)
        flash("테스크 참여 신청되었습니다.")

        return redirect("/")
    else:
        flash("개인정보 활용에 동의하셔야 테스크에 참여가 가능합니다.")
        return redirect("/")

@controller.route("/my_task", methods=["GET"])
def get_my_task_submitter():
    user_index = int(request.cookies.get("user_index"))
    tasks = services.submitter.participating_tasklist(user_index)

    return render_template("submitter/my_task.html", tasks=tasks)


@controller.route("/submit_task", methods=["POST"])
def submit_task():

    try:
        # new task processing code
        file = request.files['file']
        fname = secure_filename(file.filename)
        path = os.path.join(UPLOAD_DIR + "/odsf/", fname)
        file.save(path)
    except:
        flash("파일 업로드가 실패했습니다.")
        return redirect("/")
    

    validation = system_estimator.statistic.check_validate(fname)

    # check duplicate tuple
    if not validation['duplicate_ratio']:
        flash("중복 튜플 비율이 기준을 벗어납니다.")
        return redirect("/")

    # check null ratio
    rejects = []
    for c, v in validation.items():
        if c != "duplicate_ratio" and not v:
            rejects.append(c)

    if len(rejects) != 0:
        flash(f"{rejects} 컬럼의 Null 값 비율이 기준을 벗어납니다.")
        return redirect("/")
    
    # data is validate
    

        

        



    flash("제출이 완료되었습니다. ㅅㄱ~ 그만 집에 보내줘...")

    return redirect("/")


@controller.route("/task/download")
def csv_file_download_with_stream():

    odsf_type_id = int(request.args.get('odsf_type_id', 0))

    if odsf_type_id != 0:
        odsf_type = services.submitter.odsf_type_schema_info(odsf_type_id)
    else:
        return redirect("/my_task")

    filename = f"{odsf_type['TaskName']}_{odsf_type['DataTypeName']}"

    # schema에 맞는 df 생성
    #승수형 기다리기
    schema = json.loads(odsf_type['MappingInfo'])
    schema = list(schema.keys())
    temp_df = pd.DataFrame(columns=schema)

    # dataframe을 저장할 IO stream 
    output_stream = StringIO()

    # 그 결과를 앞서 만든 IO stream에 저장
    temp_df.to_csv(output_stream, index=False)
    response = Response(
        output_stream.getvalue(),
        mimetype='text/csv',
        content_type='application/octet-stream',
    )

    response.headers["Content-Disposition"] = f"attachment; filename={filename}.csv"

    return response
