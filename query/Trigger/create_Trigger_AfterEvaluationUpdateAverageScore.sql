-- 평가자 평가 완료시마다 평균 데이터 품질 점수 계산하여 업데이트

DELIMITER //

CREATE Trigger AfterUsingCoupon
AFTER UPDATE ON EVALUATION
FOR EACH ROW
	Begin
		IF NEW.Status == 'done' THEN
			


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
        