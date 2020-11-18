from database.connection import connect

# connect to db
connect = connect()
cursor = connect.cursor()

def tasklist_detail(user_id):
    #진행 중인 태스크에 index, taskname, deadline
    #참여상태(진행중, 대기중, 거절됨.. 이거는 버튼에 반영) 보여주기 
    sql = "SELECT ROW_NUMBER() AS num, T.TaskName, T.Deadline, P.Status FROM TASK AS T LEFT JOIN PARTICIPATION AS P ON P.FK_TaskName = T.TaskName WHERE P.FK_idUSER = %s"
    cursor.execute(sql, (user_id))
    data = cursor.fetchall()
    return data

def participating_tasklist():
    #간단한 태스크 정보 index, taskname, deadline, submit_num, pass 수
    sql = "SELECT ROW_NUMBER() AS num, TaskName"
    pass

def task_info():
    #태스크 정보
    
    pass

def leaderboard():
    #특정 태스크의 전체 참여자의 제출 현황
    #index, 제출자 id, 원본 데이터 타입, 평가점수, pass여부
    #점수 순으로 sorting
    pass

def my_submission_list():
    #회차, 기간, 제출파일명, 원본데이터타입, 날짜, 시스템점수, 평가자점수(평균), total 점수, pass여부
    #원본데이터타입별로 sorting(전체, 타입 1, 타입2)
    #pass 여부별로 sorting
    pass

def score_detail():
    #시스템점수 상세 보기
    pass

def submit_info():
    #taskname, 스키마 정보, 매핑 정보
    pass

def submit():
    #제출자 파일을 받으면 origin_dsf로 저장
    pass

