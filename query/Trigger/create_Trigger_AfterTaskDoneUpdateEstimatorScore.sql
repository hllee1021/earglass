-- after task is done, update user score

DELIMITER //

CREATE TRIGGER AfterTaskDoneUpdateEstimatorScore
AFTER UPDATE ON TASK
FOR EACH ROW
BEGIN
    DECLARE varEstimatorrNum
    varFK_idEstimator
    varFileNum
varEvaluationNum
varAvgScore
varSTDScore
varSmallIndex
varNormZ
varOulierCount

    SET curTaskName = NEW.TaskName;
    SET varIndex = 0;

    IF (NEW.Status = 'done') THEN

        SELECT  COUNT(*) INtO varEstimatorrNum
        FROM EstimatorsInDoneTask
        WHERE TaskName = curTaskName;

        myloop: LOOP
            SET varIndex = varIndex + 1;

            SELECT FK_idEstimator INTO varFK_idEstimator
            FROM EstimatorsInDoneTask
            WHERE TaskName = curTaskName
            AND IndexNum = varIndex;

            -- 배정 개수 계산
            SELECT COUNT(*) INTO varFileNum
            FROM EVALUATION
            WHERE FK_idEstimator = varFK_idEstimator
            AND FK_idPARSING_DSF IN (SELECT idPARSING_DSF 
                                    FROM PARSING_DSF
                                    WHERE TaskName = curTaskName);

            -- 평가 개수 계산
            SELECT COUNT(*) INTO varEvaluationNum
            FROM EVALUATION
            WHERE FK_idEstimator = varFK_idEstimator
            AND Status = 'done'
            AND FK_idPARSING_DSF IN (SELECT idPARSING_DSF 
                                    FROM PARSING_DSF
                                    WHERE TaskName = curTaskName);

            SELECT AVG(Score) INTO varAvgScore, STD(Score) INTO varSTDScore
            FROM EVALUATION
            WHERE Status = 'done' 
            AND FK_idPARSING_DSF IN (SELECT idPARSING_DSF 
                                    FROM PARSING_DSF
                                    WHERE TaskName = curTaskName);

            SET varSmallIndex = 0;
            SET varOulierCount = 0;

            smallloop: LOOP
                SET varSmallIndex = varSmallIndex + 1;

                SELECT ABS((Score - varAvgScore)/varSTPScore) INTO varNormZ
                FROM EVALUATION
                WHERE FK_idEstimator = varFK_idEstimator
                AND Status = 'done'
                AND FK_idPARSING_DSF IN (SELECT idPARSING_DSF 
                                    FROM PARSING_DSF
                                    WHERE TaskName = curTaskName);

                IF varNormZ > 1 THEN
                    SET varOulierCount = varOulierCount + 1;
                END IF;

                IF varSmallIndex = varEvaluationNum THEN
                    LEAVE smallloop;
                END IF;
            END LOOP smallloop;


            
            -- total score 평균 계산
            SELECT MAX(TotalScore) INTO varMaxTotalScore
            FROM PARSING_DSF
            WHERE TaskName = curTaskName
            AND TotalStatus = 'done';

            SELECT AVG(TotalScore) INTO varAvgTotalScore
            FROM PARSING_DSF
            WHERE TaskName = curTaskName
            AND SubmitterID = varSubmitterID
            AND TotalStatus = 'done';

            -- 제출 수 비율
            IF varSubmitNum > 100 THEN
                SET varSubmitNumRatio = 1;
            ELSE
                SET varSubmitNumRatio = (900+varSubmitNum)/1000;
            END IF;

            SET newSubmitterScore = (varPassNum/varSubmitNum)*40
            + 50*(varAvgTotalScore/varMaxTotalScore)
            + 10*varSubmitNumRatio;

            UPDATE USER
                SET UserScore = 0.85*UserScore + 0.15*newSubmitterScore
                WHERE idUSER = varSubmitterID;

            IF varIndex = varSubmitterNum THEN
                LEAVE myloop;
            END IF;
        END LOOP myloop;
    END IF;
END; //

DELIMITER ;


