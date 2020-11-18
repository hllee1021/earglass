from database.connection import *
import math


def get_users():
    # 전체 USER 상세 정보 리턴
    sql = "SELECT Id, Name, Gender, BirthDate, PhoneNum, Address, UserScore \
            FROM USER WHERE FK_UserTypeName != \'관리자\'"
    return queryall(sql)


def show_submitter(user_id):
    # Submitter 에 대한 상세 정보 및 참여중인 task 열람
    sql = "SELECT Id, Name, Gender, BirthDate, PhoneNum, Address, UserScore \
            FROM USER WHERE Id = %s and FK_UserTypeName = \'제출자\'"
    return queryall(sql, (user_id))
    

def show_estimator(user_id):
    # Estimator에 대한 상세 정보 및 참여중인 task 열람
    sql = "SELECT Id, Name, Gender, BirthDate, PhoneNum, Address, UserScore \
            FROM USER WHERE Id = %s and FK_UserTypeName = \'평가자\'"
    return queryall(sql, (user_id))


def show_estimate_status(user_id, page):
    # 평가자 평가파일 현황
    sql = "SELECT * FROM EVALUATION WHERE FK_idUSER = %s LIMIT %s OFFSET %s"
    cursor.execute(sql, (user_id, 20, 20*int(page)))    
    data = cursor.fetchall()
    return data


def show_submit_status(user_id):
    # 제출자 제출 현황
    sql = "SELECT * FROM ORIGIN_DSF WHERE FK_idUSER = %s"
    cursor.execute(sql, (int(user_id)))
    data = cursor.fetchone()
    return data 

def show_task():
    #taskname, task 통계(제출 파일 수, pass된 파일 수), task data table 위치
    sql = "SELECT TaskName, COUNT(*) AS TotalSubmitNum, "

    pass

def show_task_detail():
    #정보 다 보여주기
    pass

def sort_by_origin_data_type():
    #원본 데이터 타입 별로 보여주기
    #제출 파일 수, pass된 파일 수
    pass

def edit_task():
    #수정된 정보 update
    #taskname, description, 최소업로드주기, table 이름, 스키마, 원본 데이터 타입
    pass

def add_origin_data_type():
    #각 태스크에 원본 데이터 타입 추가
    pass

def delete_task():
    #task delete
    pass

def show_task_participation_list():
    #index, 참여자 id, 제출자 평가 점수
    pass

def sort_task_participation_list():
    #참여 상태별로 sorting
    pass

def show_submitter_task():
    #각 제출자가 참여 중인 태스크 보여주기
    #태스크 통계정보 다 보여줘야 함
    #index, taskname, 제출 수, pass된 파일 수 
    #통계정보 누르면 원본 데이터 타입 별로 제출 수, pass된 파일 수
    pass

def add_task():
    #태스크 추가
    #taskname, description, 최소업로드주기, table 이름, 스키마, 원본 데이터 타입, 시스템 pass 기준, 평가자 pass 기준
    pass

