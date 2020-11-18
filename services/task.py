from database.connection import *

# connect to db
connect = connect()
cursor = connect.cursor()

# Show Task
def get_TaskPage():
    # 테스크 페이지 수 리턴
    sql = "SELECT COUNT(*) AS C FROM TASK"
    cursor.execute(sql)
    data = math.ceil(float(cursor.fetchone()["C"])/20)
    return data


def get_tasks(page):
    # 페이지 번호에 따른 task 리턴
    sql = "SELECT * FROM TASK LIMIT %s OFFSET %s"
    cursor.execute(sql, (20, 20*int(page)))    
    data = cursor.fetchall()
    return data

    
def task_detail(task_id):
    # 테스크 관련 정보 모두 불러오기
    sql = "SELECT * FROM TASK T WHERE T.TaskName = %s"
    return queryone(sql, (task_id,))




### Task Add, Delete, Update
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



def apply_task():
    # 제출자가 테스크를 신청
    pass


def applied_submitter(task_id):
    # task를 신청한 제출자 목록
    pass

def authorized_submitter(task_id):
    # task 참가가 허가된 제출자 목록
    pass
