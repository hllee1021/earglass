-- after evaluation is updated, update total status
DELIMITER //

CREATE TRIGGER AfterEvaluationUpdateTotalStatus
AFTER UPDATE ON EVALUATION
FOR EACH ROW
BEGIN
    DECLARE     curFK_idPARSING_DSF     Int(11);
    DECLARE     curCountEvaluationNum   Int(11);

    SET curFK_idPARSING_DSF = NEW.FK_idPARSING_DSF;

    SELECT COUNT(*) INTO curCountEvaluationNum
    FROM EVALUATION
    WHERE FK_idPARSING_DSF = curFK_idPARSING_DSF AND Status = 'done';

    IF (curCountEvaluationNum = 3) THEN
        UPDATE PARSING_DSF
        SET TotalStatus = 'done'
        WHERE idPARSING_DSF = curFK_idPARSING_DSF;
    END IF;
END
//

DELIMITER ;