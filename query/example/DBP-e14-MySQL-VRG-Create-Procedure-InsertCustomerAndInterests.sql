DELIMITER //

CREATE PROCEDURE InsertCustomerAndInterests
	    (IN newLastName		 Char(25),
	     IN newFirstName	 Char(25),
         IN newEmailAddress	 Varchar(100),
	     IN newAreaCode		 Char(3),
	     IN newPhoneNumber 	 Char(8),		 
		 IN newNationality 	 Char(30))

BEGIN

  DECLARE	varRowCount		Int;
  DECLARE	varArtistID	  	Int;
  DECLARE	varCustomerID	Int;
  DECLARE  	done           	Int DEFAULT 0;
  DECLARE  	ArtistCursor   	CURSOR FOR
					   SELECT	 ArtistID
					   FROM	   	 ARTIST
					   WHERE	 Nationality=newNationality;
  DECLARE  	continue   HANDLER FOR NOT FOUND SET done = 1;

  # Check to see if Customer already exist in database

	SELECT		COUNT(*) INTO varRowCount
	FROM	  	CUSTOMER
	WHERE	  	LastName = newLastName
		AND	  	FirstName = newFirstName
        AND   	EmailAddress =	newEmailAddress
		AND   	AreaCode = newAreaCode
		AND   	PhoneNumber = newPhoneNumber;
		

	# IF (varRowCount > 0) THEN Customer already exists.
	IF (varRowCount > 0) THEN
		ROLLBACK;
		SELECT 'Customer already exists';
	END IF;

  # IF (varRowCount = 0) THEN Customer does not exist.
  # Insert new Customer data.

  IF (varRowCount = 0) THEN
        INSERT INTO CUSTOMER (LastName, FirstName, EmailAddress, AreaCode, PhoneNumber, Country)
            VALUES(newLastName, newFirstName,  newEmailAddress, newAreaCode, newPhoneNumber, newNationality);

        # Get new CustomerID surrogate key value.

        SET varCustomerID = LAST_INSERT_ID();

        # Create intersection record for each appropriate Artist.

        OPEN	ArtistCursor;
				REPEAT
                FETCH ArtistCursor INTO varArtistID;
                    IF NOT done THEN
                        INSERT INTO CUSTOMER_ARTIST_INT (ArtistID, CustomerID)
                            VALUES(varArtistID, varCustomerID);
                        END IF;
                UNTIL done END REPEAT;
        CLOSE	ArtistCursor;

        SELECT 'New customer and artist interest data added to database.'
            AS InsertCustomerAndInterstsResults;
        END IF;
END
//

DELIMITER ;

