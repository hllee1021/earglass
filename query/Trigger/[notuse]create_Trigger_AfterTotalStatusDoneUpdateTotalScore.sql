-- -- after total status becomes 'done', update total score

-- CREATE TRIGGER AfterTotalStatusDoneUpdateTotalScore
-- AFTER UPDATE ON PARSING_DSF
-- FOR EACH ROW
-- BEGIN

--     DECLARE     curidPARSING_DSF    Int(11);
--     DECLARE     curSystemScore      Float;
--     DECLARE     curAverageScore     Float;

--     SET curidPARSING_DSF = NEW.idPARSING_DSF;
--     SET curSystemScore = NEW.SystemScore;
--     SET curAverageScore = NEW.AverageScore;

--     IF NEW.TotalStatus = 'done' THEN
--         UPDATE PARSING_DSF 
--         SET TotalScore = 0.4*curSystemScore + 0.6*curAverageScore 
--         WHERE idPARSING_DSF = curidPARSING_DSF;
--     END IF;
-- END; //

-- DELIMITER ;