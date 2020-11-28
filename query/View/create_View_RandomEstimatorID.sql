-- estimators in done task

CREATE VIEW RandomEstimatorID AS
    SELECT idUSER, ROW_NUMBER() OVER() AS IndexNum
    FROM USER
    WHERE FK_UserTypeName = '평가자'
    ORDER BY RAND()
    LIMIT 3;