DELIMITER //

CREATE FUNCTION FirstNameFirst
-- These are the input parameters
		(
		 varFirstName		Char(25),
		 varLastName		Char(25)
		)
RETURNS Varchar(60) DETERMINISTIC
BEGIN 
	-- This is the variable that will hold the value to be returned
	DECLARE	varFullName	Varchar(60);
	-- SQL statements to concatenate the names in the proper order
	SET varFullName = CONCAT(varFirstName, ' ', varLastName);
	-- Return the concatenated name
	RETURN varFullName;

END
//

DELIMITER ;

/* *** SQL-Query-CH10C-01 *** */

SELECT 		CONCAT(FirstName, ' ', LastName) AS CustomerName,
			Street, City, State, ZIPorPostalCode
FROM		CUSTOMER
ORDER BY	CustomerName;

/* *** SQL-Query-CH10C-02 *** */

SELECT 		FirstNameFirst(FirstName, LastName) AS CustomerName,
			Street, City, State, ZIPorPostalCode
FROM		CUSTOMER
ORDER BY	CustomerName;

/* *** SQL-Query-CH10C-03 *** */

SELECT		FirstNameFirst(FirstName, LastName) AS ArtistName,
			DateofBirth, DateDeceased
FROM		ARTIST
ORDER BY	ArtistName;

/* *** SQL-Query-CH10C-04 *** */

SELECT		FirstNameFirst(C.FirstName, C.LastName) AS CustomerName,
			FirstNameFirst(A.FirstName, A.LastName) AS ArtistName
FROM		CUSTOMER AS C JOIN CUSTOMER_ARTIST_INT AS CAI
	ON		C.CustomerID = CAI.CustomerID
			JOIN	ARTIST AS A
				ON	CAI.ArtistID = A.ArtistID
ORDER BY	CustomerName, ArtistName;

/*********************************************************************************/

DELIMITER //

CREATE FUNCTION GetLastNameCommaSeparated

-- These are the input parameters
(
	varName			VARCHAR(45)
)
RETURNS VARCHAR(25) DETERMINISTIC
BEGIN
	-- This is the variable that will hold the value to be returned
	DECLARE varLastName		VARCHAR(25);

	-- This is the variable that will hold the position of the comma
	DECLARE varIndexValue	INT;

	-- SQL statement to find the comma deparator 

	SET varIndexValue = LOCATE(',', varName);
	
	-- SQL statement to determine last name
	SET varLastName = SUBSTRING(varName, 1, (varIndexValue - 1));

	-- Return the last name
	RETURN varLastName;
END
//

DELIMITER ;

/* *** SQL-Query-CH10C-05 *** */

SELECT		ArtistName,
			GetLastNameCommaSeparated(ArtistName) AS ArtistLastName 
FROM		POSTCARDS_TEMP
ORDER BY	ArtistName;

/* *** SQL-ALTER-TABLE-CH10A-01 *** */

ALTER TABLE POSTCARDS_TEMP
	ADD		ArtistLastName		Char(25)		NULL;
    
/* *** SQL-ALTER-TABLE-CH10A-02 *** */
    
ALTER TABLE POSTCARDS_TEMP
	ADD		ArtistID				Int			NULL;
    
SELECT 		*	
FROM		POSTCARDS_TEMP;


/* *** SQL-UPDATE-CH10A-01 *** */

UPDATE		POSTCARDS_TEMP
	SET		ArtistLastName = GetLastNameCommaSeparated(ArtistName);
    
/* *** SQL-UPDATE-CH10A-02 *** */

UPDATE		POSTCARDS_TEMP
	SET		ArtistID =  
				(SELECT	ArtistID 
				 FROM	ARTIST
				 WHERE	ARTIST.LastName = POSTCARDS_TEMP.ArtistLastName);

SELECT 		*	
FROM		POSTCARDS_TEMP;











