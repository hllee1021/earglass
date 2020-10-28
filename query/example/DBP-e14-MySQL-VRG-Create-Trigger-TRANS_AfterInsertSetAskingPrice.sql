DELIMITER //

CREATE TRIGGER AfterTRANSInsertSetAskingPrice
AFTER INSERT ON TRANS
FOR EACH ROW

BEGIN

    DECLARE	varRowCount		      Int;
    DECLARE	varPriorRowCount	  Int;
    DECLARE varWorkID			  Int;
	DECLARE	varTransactionID	  Int;
	DECLARE	varAcquisitionPrice	  Numeric(8,2);
	DECLARE	varNewAskingPrice	  Numeric(8,2);
	DECLARE	varSumNetProfit		  Numeric(8,2);
	DECLARE	varAvgNetProfit		  Numeric(8,2);
	
	SET     varTransactionID = NEW.TransactionID;
    SET		varAcquisitionPrice = NEW.AcquisitionPrice;
	SET     varWorkID = NEW.WorkID;

	# First find if work has been here before.


	SELECT 		COUNT(*) INTO varRowCount
	FROM	   	TRANS
	WHERE	  	WorkID = varWorkID;

	SET varPriorRowCount = (varRowCount - 1);


	# If varPriorRowCount = 0 this is a new acquistion.
	IF (varPriorRowCount = 0) THEN
		# Set @NewAskingPrice to twice the acquisition cost.
		SET varNewAskingPrice = (2 * varAcquisitionPrice);
	ELSE
		# The work has been here before
		# We have to determine the value of varNewAskingPrice

		SELECT    	SUM(NetProfit) INTO varSumNetProfit
		FROM		ArtistWorkNetView AS AWNV
		WHERE		AWNV.WorkID = varWorkID
		GROUP BY	AWNV.WorkID;

		SET varAvgNetProfit = (varSumNetProfit / varPriorRowCount);

		# Now choose larger value for the new AskingPrice.

		IF ((varAcquisitionPrice + varAvgNetProfit)
				> (2 * varAcquisitionPrice)) THEN
			SET varNewAskingPrice = (varAcquisitionPrice + varAvgNetProfit);
		ELSE
			SET varNewAskingPrice = (2 * varAcquisitionPrice);
			END IF;
		END IF;

  # Update PRICELIST with the value of AskingPrice

	INSERT INTO PRICELIST VALUES (varTransactionID, 0);

	UPDATE PRICELIST
		SET		AskingPrice = varNewAskingPrice
		WHERE	TransactionID = varTransactionID;

END
//

DELIMITER ;