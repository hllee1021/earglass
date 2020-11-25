-- estimators in done task

CREATE VIEW RandomEstimatorID AS
    SELECT RAND() AS random, idUSER, ROW_NUMBER() OVER() AS IndexNum
    FROM USER
    WHERE FK_UserTypeName = '평가자'
    ORDER BY random
    LIMIT 3;

