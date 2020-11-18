from database.connection import *

# connect to db
connect = connect()
cursor = connect.cursor()

def tasklist_detail(user_id):
    #진행 중인 태스크에 taskname, deadline
    #참여상태(진행중, 대기중, 거절됨.. 이거는 버튼에 반영) 보여주기 
    sql = "SELECT T.TaskName, T.Deadline, P.Status \
    FROM TASK AS T LEFT JOIN PARTICIPATION AS P ON P.FK_TaskName = T.TaskName WHERE P.FK_idUSER = %s"
    return queryall(sql, (user_id))

def participating_tasklist():
    #간단한 태스크 정보 taskname, deadline, submit_num, pass 수
    sql = "SELECT T.TaskName, T.Deadline, MAX(P.SubmitNum) AS submit_num, \
    SUM(CASE Pass WHEN 'P' THEN 1 ELSE 0 END) AS pass_num\
    FROM TASK AS T LEFT JOIN PARSING_DSF AS P ON P.FK_TaskName = T.TaskName"
    return queryall(sql)

def task_info(task_name):
    #태스크 정보
    sql = "SELECT TaskName, Description, MinPeriod, Status, TaskDataTableName, TaskDataTableSchemaInfo, TaskDataTableLocation, Deadline \
    FROM TASK WHERE TaskName = %s"
    return queryone(sql, (task_name))

def leaderboard(task_name):
    #특정 태스크의 전체 참여자의 제출 현황
    #제출자 id, 원본 데이터 타입, 평가점수, pass여부
    #점수 순으로 sorting
    sql = "SELECT P.SubmitterID, O.DataTypeName, P.TotalScore, P.Pass \
    FROM PARSING_DSF AS P LEFT JOIN ORIGIN_DATA_TYPE AS O ON P.OriginDataTypeID = O.idORIGIN_DATA_TYPE \
    WHERE P.TaskName = %s ORDER BY P.TotalScore DESC"
    return queryall(sql, (task_name))

def my_submission_list():
    #회차, 기간, 제출파일명, 원본데이터타입, 날짜, 시스템점수, 평가자점수(평균), total 점수, pass여부
    #원본데이터타입별로 sorting(전체, 타입 1, 타입2)
    #pass 여부별로 sorting
    pass

def score_detail():
    #시스템점수 상세 보기
    pass

def submit_info(task_name):
    #taskname, 스키마 정보, 매핑 정보
    sql = "SELECT TaskName, SchemaInfo, MappingInfo FROM ORIGIN_DATA_TYPE WHERE TaskName = %s"
    return queryone(sql, (task_name))

def submit():
    #제출자 파일을 받으면 origin_dsf로 저장
    pass

