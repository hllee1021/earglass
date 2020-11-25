-- estimators in done task

CREATE VIEW EstimatorsInDoneTask AS
    SELECT ROW_NUMBER() OVER() AS IndexNum, T.TaskName, DISTINCT E.FK_idEstimator
    FROM TASK AS T, EVALUATION AS E, PARSING_DSF AS P
    WHERE T.Status = 'done'
    AND T.TaskName = P.TaskName
    AND P.idPARSING_DSF = E.FK_idPARSING_DSF;

