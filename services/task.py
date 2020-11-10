from database.connection import connect

# connect to db
connect = connect()
cursor = connect.cursor()


def get_tasks(page):
    # 페이지 번호에 따른 task 리턴
    sql = "SELECT * FROM TASK LIMIT %s OFFSET %s"
    cursor.execute(sql, (20, 20*int(page)))    
    data = cursor.fetchall()
    return data


def task_detail():
    # 테스크 관련 정보 모두 불러오기
    pass

def apply_task():
    # 제출자가 테스크를 신청
    pass

def applied_submitter(task_id):
    # task를 신청한 제출자 목록
    pass

def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass
def ():
    pass