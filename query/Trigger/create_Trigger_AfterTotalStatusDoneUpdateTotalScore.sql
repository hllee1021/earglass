-- after total status becomes 'done', update total score

CREATE TRIGGER AfterTotalStatusDoneUpdateTotalScore
AFTER UPDATE ON PARSING_DSF
FOR EACH ROW
BEGIN
    IF NEW.TotalStatus != OLD.TotalStatus THEN
        UPDATE PARSING_DSF SET TotalScore = NEW.TotalScore WHERE idPARSING_DSF = OLD.idPARSING_DSF;
    END IF;
END; //

DELIMITER ;