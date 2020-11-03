from database.connection import connect

def get_tasks(page):
    # 페이지 번호에 따른 task 리턴
    conn = connect()
    cur = conn.cursor()
    sql = "SELECT * FROM TASK LIMIT %s OFFSET %s"
    cur.execute(sql, (20, 20*int(page)))    
    data = cur.fetchall()
    return data


def get_users(page):
    # 페이지 번호에 따른 user 리턴
    pass


def get_UserPage():
    # 유저 페이지 수 리턴
    pass


def get_TaskPage():
    # 테스크 페이지 수 리턴
    pass


def searchUser(column, search_word, page):
    # column에 word로 검색한 결과를 page에 따라 리턴
    pass


def show_submitter(user_id):
    # Submitter 에 대한 상세 정보 열람
    pass


def show_estimator(user_id):
    # Estimator에 대한 상세 정보 열람
    conn = connect()
    cur = conn.cursor()
    sql = "SELECT * FROM USER WHERE idUSER = %s"
    cur.execute(sql, user_id)   
    data = cur.fetchall()
    return data


def add_task(task_name, description, min_period, manager_id):
    # 테스크 생성
    conn = connect()
    cur = conn.cursor()
    cur.callproc('InsertNewTask', (task_name, description, min_period, manager_id))    
    message = cur.fetchall()
    conn.commit()
    return message


def remove_task(task_name):
    # 테스크 제거
    conn = connect()
    cur = conn.cursor()
    cur.callproc('DeleteTask', (task_name,) )
    message = cur.fetchall()
    conn.commit()
    return message


def edit_task(task_name, description, min_period):
    # 테스크 수정
    conn = connect()
    cur = conn.cursor()
    cur.callproc('EditTask', (task_name, description, min_period))
    message = cur.fetchall()
    conn.commit()
    return message

def update_task_status(task_name, status):
    # 테스크 상태 업데이트
    conn = connect()
    cur = conn.cursor()
    cur.callproc('UpdateTaskStatus', task_name)
    message = cur.fetchall()
    conn.commit()
    return message

def show_estimate_status(user_id):
    # 평가자 평가파일 현황
    conn = connect()
    cur = conn.cursor()
    sql = "SELECT * FROM TASK LIMIT %s OFFSET %s"
    cur.execute(sql, (20, 20*int(page)))    
    data = cur.fetchall()
    return data


def show_submit_status(user_id):
    # 제출자 제출 현황
    conn = connect()
    cur = conn.cursor()
    sql = "SELECT * FROM TASK LIMIT %s OFFSET %s"
    cur.execute(sql, (20, 20*int(page)))    
    data = cur.fetchall()
    return data
