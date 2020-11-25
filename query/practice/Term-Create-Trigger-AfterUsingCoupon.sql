DELIMITER //

/*DROP Trigger IF EXISTS AfterUsingCoupon;*/

CREATE Trigger AfterUsingCoupon
AFTER UPDATE ON Transaction
FOR EACH ROW
	Begin
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
        