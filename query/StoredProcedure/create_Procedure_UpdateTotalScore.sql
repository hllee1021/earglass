--total score 업데이트

DELIMITER //

CREATE PROCEDURE UpdateTotalScore
            (IN     varSystemScore      Float,
             IN     varAverageScore     Float,
             IN     varidPARSING_DSF    Int(11))

checkexist: BEGIN

    --check iff systemscore and averagescore exists
    IF varSystemScore = NULL OR varAverageScore = NULL THEN
        SELECT 'score does not exist'
        AS ScoreDoesNotExistMessage;
        ROLLBACK;
        LEAVE checkexist;
    END IF;

    --update total score
    UPDATE PARSING_DSF
        SET TotalScore = (varSystemScore+varAverageScore)/2
        WHERE idPARSING_DSF = varidPARSING_DSF;

END
//

DELIMETER ;