DELIMITER //

CREATE PROCEDURE UpdateCustomerName
			(IN		oldCustomerLastName	    Char(25),
			 IN		oldCustomerFirstName	Char(25),
			 IN		newCustomerLastName	    Char(25),
			 IN		newCustomerFirstName	Char(25))

BEGIN

	DECLARE	varRowCount	 Int;

	# Count number of synonyms in CUSTOMER.
	SELECT    COUNT(*) INTO varRowCount
	FROM	  CUSTOMER AS C1
	WHERE	  C1.LastName = oldCustomerLastName
		AND	  C1.FirstName = oldCustomerFirstName
		AND	  EXISTS
			  (SELECT	  	*
			   FROM	 	  	CUSTOMER AS C2
               WHERE	  	C1.LastName = C2.LastName
                    AND		C1.FirstName = C2.FirstName
                    AND		C1.CustomerID <> C2.CustomerID);

	IF (varRowCount >= 1) THEN
		# This is a problem account.
		# Rollback the transaction.
		ROLLBACK;
		# Print message
		SELECT 'Duplicate customer name - Contact the manager.'
		AS UpdateCustomerNameWarningMessage;
	ELSE
		# The Customer last name is unique.
		# Update the Customer record.
		UPDATE	CUSTOMER
		  SET		  LastName = newCustomerLastName,
					  FirstName = newCustomerFirstName
		  WHERE		  LastName = oldCustomerLastName
			    AND	  FirstName = oldCustomerFirstName;
		# Print message
		SELECT 'Customer name updated successfully.'
		AS UpdateCustomerNameSuccessfulMessage;
		END IF;

END
//

DELIMITER ;

