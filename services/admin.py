from database.connection import connect

# connect to db
connect = connect()
cursor = connect.cursor()
import math


def get_users(page):
    # 페이지 번호에 따른 user 리턴
    sql = "SELECT * FROM USER LIMIT %s OFFSET %s"
    cursor.execute(sql, (20, 20*int(page)))    
    data = cursor.fetchall()
    return data


def get_UserPage():
    # 유저 페이지 수 리턴
    sql = "SELECT COUNT(*) AS C FROM USER"
    cursor.execute(sql)
    data = math.ceil(float(cursor.fetchone()["C"])/20)
    return data


def searchUser(column, search_word, page):
    # column에 word로 검색한 결과를 page에 따라 리턴
    sql = f"SELECT * FROM USER WHERE {column} = %s LIMIT %s OFFSET %s"
    cursor.execute(sql, (search_word, 20, 20*int(page)))
    data = cursor.fetchall()
    return data


def show_submitter(user_id):
    # Submitter 에 대한 상세 정보 열람
    sql = "SELECT * FROM USER WHERE idUSER = %s and FK_TypeName = \'제출자\'"
    cursor.execute(sql, (int(user_id)))
    data = cursor.fetchone()
    return data


def show_estimator(user_id):
    # Estimator에 대한 상세 정보 열람
    sql = "SELECT * FROM USER WHERE idUSER = %s and FK_TypeName = \'평가자\'"
    cursor.execute(sql, user_id)   
    data = cursor.fetchall()
    return data


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
    #index, taskname, task 통계(제출 파일 수, pass된 파일 수), task data table 위치
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

