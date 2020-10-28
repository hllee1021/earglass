DELIMITER //

CREATE PROCEDURE TransWithCheckIsProblemAccount
			(IN		transTransactionID		Int,
			 IN		transCustomerID			Int,
			 IN		transDateSold			Date,
			 IN		transSalesPrice			Numeric(8,2))

BEGIN

	DECLARE	varIsProblemAccount	BOOLEAN;

	# Obtain value of varIsProblemAcocunt.

	SELECT 	isProblemAccount INTO varIsProblemAccount
	FROM	CUSTOMER
	WHERE	CustomerID = transCustomerID;

	IF (varIsProblemAccount = 1) THEN
		# This is a problem account.
		# Rollback the transaction.
		ROLLBACK;
		# Print message
		SELECT 'Contact the manager immediately - Customer account problems.'
		AS TransWithCheckIsProblemAccountWarningMessage;
	ELSE
		# This is a good account.
		# Complete the transaction.
		# Update TRANS with the values of CustomerID, DateSold and SalesPrice
		UPDATE  TRANS
			SET	  CustomerID = transCustomerID,
            DateSold = transDateSold,
	    			SalesPrice = transSalesPrice
			WHERE TransactionID = transTransactionID;
		# Print message
		SELECT 'Transaction complete successfully.'
		AS TransWithCheckIsProblemAccountSuccessfullTransactionMessage;
	END IF;

END
//

DELIMITER ;

