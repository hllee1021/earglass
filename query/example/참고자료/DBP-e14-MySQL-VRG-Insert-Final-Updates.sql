/* Final Application Logic updates                            */

/* UPDATE Melinda Bench data and complete transaction         */

/* *** SQL-UPDATE-CH10C-03 *** */

UPDATE	CUSTOMER
    SET		isProblemAccount = 0
    WHERE	LastName	= 'Bench'
        AND	FirstName	= 'Melinda';


/* *** SQL-UPDATE-CH10C-04 *** */

 UPDATE	TRANS
    SET		DateSold = '2014-11-18',
            SalesPrice = 475.00,
            CustomerID = 1053
    WHERE	TransactionID = 229; 
    
/* *** SQL-CALL-CH10C-05 *** */

 CALL TransWithCheckIsProblemAccount (229, 1053, '2014-11-18', 475.00);    

/* Restock a copy of this print into the gallery               */

/* *** SQL-INSERT-CH10C-07 *** */

INSERT INTO WORK (Title, Copy, Medium, Description, ArtistID)
  VALUES(
	'Color Floating in Time', '493/500', 'High Quality Limited Print',
	'Northwest School Abstract Expressionist style', 18);

-- Obtain the new WorkID

SELECT	WorkID
FROM	WORK
WHERE	 ArtistID = 18
	AND	 Title = 'Color Floating in Time '
	AND	 Copy = '493/500';

-- Use the new WorkID value (598 in this case)

/* *** SQL-INSERT-CH10C-08 *** */

INSERT INTO TRANS (DateAcquired, AcquisitionPrice, WorkID)
 	VALUES ('2015-02-05', 250.00, 598);

/* *** SQL-Query-View-CH10C-03 *** */

SELECT * FROM WorkAndTransView
ORDER BY Title, Copy;
