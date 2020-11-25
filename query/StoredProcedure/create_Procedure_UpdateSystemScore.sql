-- 파일이 제출되었을 때, system score 받아와서 DB 업데이트

DELIMITER //

CREATE PROCEDURE UpdateSystemScore
            (IN     varidPARSING_DSF    int(11),
             IN     varSystemScore      float)

invalidvalue: BEGIN
    -- If exists idPARSING_dSF
        IF EXISTS
            (SELECT * FROM PARSING_DSF
            WHERE  idPARSING_DSF = varidPARSING_DSF) THEN
                IF (varSystemScore < 0 OR varSystemScore > 100) THEN
                        SELECT 'system score is out of range'
                        AS UpdateSystemScoreErrorMessage;
                        ROLLBACK;
                        LEAVE invalidvalue;
                END IF;
            -- update systemscore
            UPDATE PARSING_DSF
                SET     SystemScore = varSystemScore
                WHERE   idPARSING_DSF = varidPARSING_DSF;
            -- print message
            SELECT 'update system score successfully'
            AS UpdateSystemScoreResults;

        ELSE
            -- print message
            SELECT 'Invalid parsing dsf id'
            AS UpdateSystemScoreErrorMessage;
        END IF;
END
//

DELIMITER ;
