from database.connection import *

def show_submit_status(user_id):
    # 제출자 제출 현황
    sql = "SELECT P.SubmitterID, P.TaskName, ODT.DataTypeName, \
    O.DateTime, O.OriginFile, P.ParsingFile, P.SubmitNum, P.Period, \
    P.Round, P.SystemScore, P.AverageScore, P.TotalScore, P.Pass, P.TotalStatus \
    FROM ORIGIN_DSF AS O, PARSING_DSF AS P JOIN ORIGIN_DATA_TYPE AS ODT ON P.OriginDataTypeID = ODT.idORIGIN_DATA_TYPE \
    WHERE O.idORIGIN_DSF = P.FK_idORIGIN_DSF AND P.SubmitterID = %s"
    return queryall(sql, (user_id, ))