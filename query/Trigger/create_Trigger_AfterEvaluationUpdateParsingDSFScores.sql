-- 평가자 평가 완료시마다 평균 데이터 품질 점수와 Total Score, PASS 계산하여 업데이트

DELIMITER //

CREATE Trigger AfterEvaluationUpdateParsingDSFScores
AFTER UPDATE ON EVALUATION
FOR EACH ROW
	Begin

		DECLARE varidEVALUATION int(11);
		DECLARE varidPARSING_DSF int(11);
		DECLARE varScoreSum int(11);
		DECLARE varAverageScore float;
		DECLARE varPassCount int(11);
		DECLARE varNonPassCount int(11);
		DECLARE varTotalPass varchar(45);

		SET varidEVALUATION = NEW.idEVALUATION;
		SET varidPARSING_DSF = NEW.FK_idPARSING_DSF;
		SET varPassCount = 0;
		SET varNonPassCount = 0;

		IF NEW.Status = 'done' THEN
			SELECT SUM(E.Score * U.UserScore) INTO varScoreSum
			FROM EVALUATION AS E, USER AS U
			WHERE E.FK_idEstimator = U.idUSER
			AND E.FK_idPARSING_DSF = varidPARSING_DSF;

			SET varAverageScore = varScoreSum / 70;
            IF varAverageScore > 100 THEN
                SET varAverageScore = 100;
            END IF;

			SELECT COUNT(*) INTO varPassCount
			FROM EVALUATION
			WHERE FK_idPARSING_DSF = varidPARSING_DSF
			AND Pass = 'P';

			SELECT COUNT(*) INTO varNonPassCount
			FROM EVALUATION
			WHERE FK_idPARSING_DSF = varidPARSING_DSF
			AND Pass = 'NP';

			IF (varPassCount - varNonPassCount) > 0 THEN
				SET varTotalPass = 'P';
			ELSE
				SET varTotalPass = 'NP';
			END IF;

			UPDATE PARSING_DSF
			SET AverageScore = varAverageScore,
				TotalScore = 0.4*SystemScore + 0.6*varAverageScore,
				Pass = varTotalPass
			WHERE idPARSING_DSF = varidPARSING_DSF;

		END IF;

END
//
DELIMITER ;
