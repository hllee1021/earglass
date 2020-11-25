-- 평가자 평가 완료시마다 평균 데이터 품질 점수와 Total Score, PASS 계산하여 업데이트

DELIMITER //

CREATE Trigger AfterUsingCoupon
AFTER UPDATE ON EVALUATION
FOR EACH ROW
	Begin

		DECLARE varidEVALUATION int(11);
		DECLARE varEstimatorNum int(11);
		DECLARE varidPARSING_DSF int(11);
		DECLARE varScoreSum int(11);
		DECLARE varAverageScore float;


		SET varidEVALUATION = NEW.idEVALUATION;
		SET varidPARSING_DSF = NEW.varidPARSING_DSF;

		IF NEW.Status = 'done' THEN
			SELECT COUNT(FK_idEstimator) INTO varEstimatorNum, SUM(Score) INTO varScoreSum
			FROM EVALUATION
			WHERE FK_idPARSING_DSF = varidPARSING_DSF;
			
			SET varAverageScore = varScoreSum / varEstimatorNum;

			IF varEstimatorNum > 1 THEN
				UPDATE PARSING_DSF
				SET AverageScore = varAverageScore
				WHERE idPARING_DSF = varidPARSING_DSF;


		DECLARE varUserID Char(36);
        DECLARE varWelcomeCoupon Char(2);
        
        SET varUserID = NEW.UserID;
        
        SELECT WelcomeCoupon INTO varWelcomeCoupon
        FROM User AS U
        WHERE varUserID =U.UserID; 
        
        IF NEW.TotalRequiredPrice <> NEW.TotalSalesPrice THEN
			IF varWelcomeCoupon = 'Y' THEN
				UPDATE USER
				SET WelcomeCoupon = 'N'
				WHERE UserID = varUserID;
			ELSE
				UPDATE USER
				SET VIPCoupon = 'N'
				WHERE UserID = varUserID;
			END IF;
        END IF;
        
END
//
DELIMITER ;
        