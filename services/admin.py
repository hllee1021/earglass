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

