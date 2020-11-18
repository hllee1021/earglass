from database.connection import *
import math
import csv
from pprint import pprint
import json


def get_users():
    '''전체 USER 상세 정보 리턴'''
    sql = "SELECT Id, Name, Gender, BirthDate, PhoneNum, Address, UserScore \
            FROM USER WHERE FK_UserTypeName != \'관리자\';"
    return queryall(sql)


def show_submitter(user_id):
    '''Submitter 에 대한 상세 정보 및 참여중인 task 열람'''
    sql = "SELECT U.Id, U.Name, U.Gender, U.BirthDate, U.PhoneNum, U.Address, U.UserScore, P.FK_TaskName \
            FROM USER AS U \
            INNER JOIN PARTICIPATION AS P \
            ON U.idUSER = P.FK_idUSER \
            WHERE U.Id = %s AND U.FK_UserTypeName = \'제출자\' \
            AND P.Status = \'ongoing\' \
            ORDER BY U.Id, P.FK_TASKName;"
    return queryall(sql, (user_id, ))


def show_estimator(user_id):
    '''Estimator에 대한 상세 정보 및 참여중인 task 열람'''
    sql = "SELECT U.Id, U.Name, U.Gender, U.BirthDate, U.PhoneNum, U.Address, U.UserScore, P.TaskName \
            FROM USER AS U INNER JOIN EVALUATION AS E \
            ON U.idUSER = E.FK_idEstimator \
            LEFT JOIN PARSING_DSF AS P\
            ON E.FK_idPARSING_DSF = P.idPARSING_DSF \
            WHERE U.Id = %s AND E.FK_UserTypeName = \'평가자\' \
            AND E.Status = \'ongoing\' \
            ORDER BY U.Id, P.TaskName;"
    return queryall(sql, (user_id, ))


def show_estimate_status(user_id):
    '''평가자 평가파일 현황'''
    sql = "SELECT * FROM EVALUATION WHERE FK_idUSER = %s"
    return queryall(sql, (user_id, ))


def show_submit_status(user_id):
    '''제출자 제출 현황'''
    sql = "SELECT P.SubmitterID, P.TaskName, ODT.DataTypeName, \
    O.DateTime, O.OriginFile, P.ParsingFile, P.SubmitNum, P.Period, \
    P.Round, P.SystemScore, P.AverageScore, P.TotalScore, P.Pass, P.TotalStatus \
    FROM ORIGIN_DSF AS O, PARSING_DSF AS P JOIN ORIGIN_DATA_TYPE AS ODT ON P.OriginDataTypeID = ODT.idORIGIN_DATA_TYPE \
    WHERE O.idORIGIN_DSF = P.FK_idORIGIN_DSF AND P.SubmitterID = %s"
    return queryall(sql, (user_id, ))

def show_task():
    '''taskname, task 통계(제출 파일 수, pass된 파일 수), task data table 위치'''
    sql = "SELECT TaskName, COUNT(*) AS TotalSubmitNum, "

    pass

def show_task_detail():
    '''정보 다 보여주기'''
    pass

def sort_by_origin_data_type():
    '''원본 데이터 타입 별로 보여주기
    제출 파일 수, pass된 파일 수'''
    pass

def edit_task():
    '''수정된 정보 update
    taskname, description, 최소업로드주기, table 이름, 스키마, 원본 데이터 타입'''
    pass


def delete_task():
    '''task delete'''
    pass

def show_task_participation_list():
    '''index, 참여자 id, 제출자 평가 점수'''
    pass

def sort_task_participation_list():
    '''참여 상태별로 sorting'''
    pass

def show_submitter_task():
    '''각 제출자가 참여 중인 태스크 보여주기
    태스크 통계정보 다 보여줘야 함
    index, taskname, 제출 수, pass된 파일 수 
    통계정보 누르면 원본 데이터 타입 별로 제출 수, pass된 파일 수'''
    pass

def add_task():
    '''태스크 추가
    taskname, description, 최소업로드주기, table 이름, 스키마, 원본 데이터 타입, 시스템 pass 기준, 평가자 pass 기준'''
    pass

def get_all_tasks():
    '''taskname, task 통계(제출 파일 수, pass된 파일 수), task data table 위치'''
    sql = "SELECT TASK.*, \
        (SELECT COUNT(TaskName) FROM PARSING_DSF WHERE PARSING_DSF.TaskName=TASK.TaskName) as ParsingDsfCount, \
        (SELECT COUNT(TaskName) FROM PARSING_DSF WHERE PARSING_DSF.Pass='P' AND PARSING_DSF.TaskName=TASK.TaskName) as PassedParsingDsfCount \
        FROM TASK"
    return queryall(sql)

def count_parsing_dsf_for_user(user_id):
    assert user_exists(user_id)
    parsing_dsfs = len(queryone("""SELECT * FROM TASK
INNER JOIN PARSING_DSF
ON TASK.TaskName=PARSING_DSF.TaskName
"""))
    return parsing_dsfs

def user_exists(user_id):
    user = queryone("SELECT * FROM USER WHERE idUSER=%d", (int(user_id), ))
    if user:
        return True
    return False

# Exists
def task_exists(task_name):
    task = queryone("SELECT * FROM TASK WHERE TaskName=%s", (task_name, ))
    if task:
        return True
    return False

def data_type_name_exists(task_name, data_type_name):
    assert task_exists(task_name)
    found = queryone("SELECT * FROM ORIGIN_DATA_TYPE WHERE TaskName=%s AND DataTypeName=%s", (task_name, data_type_name))
    if not found:
        return False
    return True

# Doesn't Exists
def get_default_fields_of_task(task_name):
    # 해당 task의 고유 스키마 정보 반환
    task = queryone("SELECT (TaskDataTableSchemaInfo) FROM TASK WHERE `TaskName`=%s", (task_name, ))
    result = task['TaskDataTableSchemaInfo'].split(',')
    return result

def set_default_fields_of_task(task_name, default_fields):
    #해당 tastk의 고유 스키마 정보 수정(삽입)
    assert task_exists(task_name)
    default_fields = ",".join(default_fields)
    execute("UPDATE TASK SET TaskDataTableSchemaInfo=%s WHERE TaskName=%s", (default_fields, task_name))

def add_origin_data_type(task_name, data_type_name, mapping_info):
    #해당 task의 원본 데이터 타입 정보 추가
    assert task_exists(task_name)
    assert not data_type_name_exists(task_name, data_type_name)
    print(mapping_info, data_type_name, task_name)
    execute("INSERT INTO ORIGIN_DATA_TYPE (MappingInfo, DataTypeName, TaskName) VALUE (%s, %s, %s)", (json.dumps(mapping_info), data_type_name, task_name))

def remove_origin_data_type(task_name, data_type_name):
    assert task_exists(task_name)
    execute("DELETE FROM ORIGIN_DATA_TYPE WHERE DataTypeName=%s AND TaskName=%s", (data_type_name, task_name))

def get_mapping_info(task_name, data_type_name):
    assert task_exists(task_name)
    assert data_type_name_exists(task_name, data_type_name)
    original_data_type = queryone("SELECT (MappingInfo) FROM ORIGIN_DATA_TYPE")
    mapping_info = original_data_type['MappingInfo']
    return mapping_info

def set_mapping_info(task_name, data_type_name, mapping_info):
    assert task_exists(task_name)
    assert data_type_name_exists(task_name, data_type_name)
    used_default_fields = set(mapping_info.values())
    allowed_default_fields = set(get_default_fields_of_task(task_name))
    print(used_default_fields.issubset(allowed_default_fields))
    if used_default_fields.issubset(allowed_default_fields):
        execute("UPDATE ORIGIN_DATA_TYPE SET MappingInfo=%s WHERE DataTypeName=%s AND TaskName=%s", (json.dumps(mapping_info), data_type_name, task_name))

