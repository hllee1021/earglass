from flask import Blueprint, render_template, redirect, request, make_response, flash
import services
from services import users
from pprint import pprint

controller = Blueprint("estimator", __name__)


@controller.route("/", methods=["GET"])
def get_estimator_home():
    user_index = int(request.cookies.get("user_index"))
    tasks = services.estimator.evaluate_waiting_list(user_index)
    pprint(tasks)
    return render_template("estimator/estimator_home.html", tasks=tasks)


@controller.route("/pdsf_detail", methods=["GET"])
def get_pdsf_detail():
    user_index = int(request.cookies.get("user_index"))
    tasks = services.estimator.evaluated_list(user_index)
    # tasks = [{"id": 1, "name":"aa","submitter_name":"hllee1021", "score":"100", "pass":"P","date":"2020/11/20"},{"id": 2, "name":"bbb","submitter_name":"1231asf", "score":"50", "pass":"N","date":"2020/12/20"},{"id": 3, "name":"lala","submitter_name":"qwe123123", "score":"70", "pass":"P","date":"2020/9/20"}]
    return render_template("estimator/pdsf_detail.html",tasks=tasks)

#made by 학림
@controller.route("/estimator_task_info", methods=["GET"])
def get_estimator_task_info():
    # task_name=request.cookies.get("task_name")
    task_name = request.args.get('task_name', 0)
    tasks=services.estimator.task_detail(task_name)
    print(tasks)
    # tasks = {"name":"im_task","description":"card data please~~ samsung good good", "schema_info":"스키마 인포 어떻게 쓰지이", "deadline":"2020/11/20","pass_cut":"중복 튜플 수에 대해서 널널하게 해도 되니까, null 비율에 엄격하게 해주세용"}
    return render_template("/estimator/estimator_task_info.html",tasks=tasks)

#made_by 학림 evaluator_home에서 평가했을때 form action 라우터
@controller.route("/evaluate", methods=["POST"])
def evaluate():
    '''학림's estimator가 평가하는 라우터'''
    score = int(request.form.get("score"))
    p_np = request.form.get("p_np")
    idPARSING_DSF = int(request.args.get('idPARSING_DSF', 0))
    user_index=int(request.cookies.get("user_index"))
    if score>100 or score<0:
        flash("점수는 0이상 100사이로 입력해야합니다")
        print(123)
        return redirect("/")
    else:
        services.estimator.update_evaluation_status(idPARSING_DSF,user_index,score,p_np)
        print(345)
        return redirect("/")
    return render_template("evaluator/evaluate_home.html")

@controller.route("/task/download")
def csv_file_download_with_stream():
    """승수형이 submitter download한거 복사함 일단"""
    idPARSING_DSF = int(request.args.get('idPARSING_DSF', 0))
    if idPARSING_DSF != 0:
        pdsf_type = services.estimator.pdsf_file_info(idPARSING_DSF)
    else:
        return redirect("/my_task")

    filename = f"{pdsf_type['TaskName']}_{pdsf_type['ParsingFile']}"

    # schema에 맞는 df 생성
    schema = json.loads(pdsf_type['MappingInfo'])
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