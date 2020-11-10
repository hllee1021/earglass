from database.connection import connect

connect = connect()
cursor = connect.cursor()
import math

def get_tasks(page):
    # 페이지 번호에 따른 task 리턴
    sql = "SELECT * FROM TASK LIMIT %s OFFSET %s"
    cursor.execute(sql, (20, 20*int(page)))    
    data = cursor.fetchall()
    return data


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


def get_TaskPage():
    # 테스크 페이지 수 리턴
    sql = "SELECT COUNT(*) AS C FROM TASK"
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
    sql = "SELECT * FROM USER WHERE idUSER = %s and FK_TypeName = \"제출자\""
    cursor.execute(sql, (int(user_id)))
    data = cursor.fetchone()
    return data 


def show_estimator(user_id):
    # Estimator에 대한 상세 정보 열람
    sql = "SELECT * FROM USER WHERE idUSER = %s"
    cursor.execute(sql, user_id)   
    data = cursor.fetchall()
    return data


def add_task(task_name, description, min_period, manager_id):
    # 테스크 생성
    cursor.callproc('InsertNewTask', (task_name, description, min_period, manager_id))    
    message = cursor.fetchall()
    connect.commit()
    return message


def remove_task(task_name):
    # 테스크 제거
    cursor.callproc('DeleteTask', (task_name,) )
    message = cursor.fetchall()
    connect.commit()
    return message


def edit_task(task_name, description, min_period):
    # 테스크 수정
    cursor.callproc('EditTask', (task_name, description, min_period))
    message = cursor.fetchall()
    connect.commit()
    return message

def update_task_status(task_name, status):
    # 테스크 상태 업데이트
    cursor.callproc('UpdateTaskStatus', (task_name, status))
    message = cursor.fetchall()
    connect.commit()
    return message

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
