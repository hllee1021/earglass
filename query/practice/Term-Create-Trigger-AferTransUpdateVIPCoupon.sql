DELIMITER //

CREATE TRIGGER AfterTransUpdateVIPCoupon
AFTER INSERT ON Transaction

FOR EACH ROW 
BEGIN

    DECLARE	rowCount				INT;
    DECLARE varUserID				Char(36);
	
	SET     varUserID = NEW.UserID;
	
	SELECT 		COUNT(*) INTO rowCount
	FROM	   	Transaction AS T1
	WHERE	  	varUserID = T1.UserID
		AND		T1.UserID IN
				(SELECT		T2.UserID
                 FROM		Transaction AS T2
				 WHERE		T1.UserID = T2.UserID
				 AND NOT	(T1.DATE <> T2.DATE
					 AND  	T1.ParkingLotID <> T2.ParkingLotID)
				);

	IF (rowCount = 10) THEN
		UPDATE User
		SET		VIPCoupon = 'Y'
		WHERE	UserID = varUserID;
	END IF;

END
//

DELIMITER ;