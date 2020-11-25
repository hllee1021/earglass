from database.connection import *

def evaluate_waiting_list(estimator_id):
    """펑가자가 평가해야 할 평가할 파일 리스트에 index, taskname, 제출자 id, deadline, ParsingFile,idPARSING_DSF"""
    sql = "SELECT ROW_NUMBER() OVER() AS num, P.TaskName, P.SubmitterID, T.Deadline, P.ParsingFile, P.idPARSING_DSF\
    FROM EVALUATION AS E, PARSING_DSF AS P LEFT JOIN TASK AS T ON P.TaskName = T.TaskName \
    WHERE P.idPARSING_DSF = E.FK_idPARSING_DSF AND E.FK_idEstimator = %s AND E.Status = 'ongoing'"
    return queryall(sql, (estimator_id, ))

def evaluated_list(estimator_id):
    """index, taskname, 제출자 id, 평가점수, pass여부, 평가날짜"""
    sql = "SELECT ROW_NUMBER() OVER() AS num, P.TaskName, P.SubmitterID, E.Score, E.Pass, E.EndTime\
    FROM EVALUATION AS E, PARSING_DSF AS P LEFT JOIN TASK AS T ON P.TaskName = T.TaskName \
    WHERE P.idPARSING_DSF = E.FK_idPARSING_DSF AND E.FK_idEstimator = %s AND E.Status = 'done'"
    return queryall(sql, (estimator_id, ))

def task_detail(task_name):
    """태스크 정보
    pass 기준 (정성)"""
    sql = "SELECT TaskName, Description, MinPeriod, Status, TaskDataTableName, TaskDataTableSchemaInfo, \
    TaskDataTableLocation, Deadline, MaxDuplicatedRowRatio, MaxNullRatioPerColumn \
    FROM TASK WHERE TaskName = %s"
    return queryone(sql, (task_name, ))

def is_done(estimator_id, parsing_dsf_id):
    """해당 파싱 파일이 평가완료되었는가?"""
    sql = "SELECT Status FROM EVALUATION WHERE FK_idEstimator = $s AND FK_idPARSING_DSF = $s"
    return queryone(sql, (int(estimator_id), int(parsing_dsf_id), ))

def done_evaluation(parsing_dsf_id, estimator_id, score, is_passed):
    """평가를 끝냈을 때 db 업데이트"""
    return callproc('UpdateEvalutionStatus', (parsing_dsf_id, estimator_id, score, is_passed))

def update_system_score():
    '''파일이 제출되었을 때, system score 계산하여 DB 업데이트'''
    pass

def update_total_score(system_score, average_score):
    '''system score과 average score을 이용해 total score 계산 후 DB 업데이트'''
    pass

# def update_estimator_score():
#     '''평가자 점수 계산 후 user 테이블 업데이트'''
#     pass

# def update_submitter_score():
#     '''제출자 점수 계산 후 user 테이블 업데이트'''
#     pass
