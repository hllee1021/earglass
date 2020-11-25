-- submitters in done task

CREATE VIEW SubmittersInDoneTask AS
    SELECT ROW_NUMBER() OVER AS INDEX, T.TaskName, P.SubmitterID
    FROM TASK AS T, PARSING_DSF AS P
    WHERE T.Status = 'done'
    AND T.TaskName = P.TaskName

