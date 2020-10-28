/* *** SQL-INSERT-CH10C-05 *** */

INSERT INTO WORK (Title, Copy, Medium, Description, ArtistID)
		VALUES
		('Spanish Dancer', '635/750', 'High Quality Limited Print',
		 'American Realist style - From work in Spain', 11);

# Obtain the new WorkID

/* *** SQL-Query-CH10C-03 *** */

SELECT		WorkID
FROM		WORK
WHERE			ArtistID = 11
		AND	  Title = 'Spanish Dancer'
		AND	  Copy = '635/750';

# Use the new WorkID value (597 in this case)
# This will fire the trigger TRANS_AfterInsertSetAskingPrice 

/* *** SQL-INSERT-CH10C-05 *** */

INSERT INTO TRANS (DateAcquired, AcquisitionPrice, WorkID)
		VALUES ('2014-11-08', 200.00, 597);
        
COMMIT;
        
# See the results in PRICELIST

/* *** SQL-Query-CH10C-09 *** */

SELECT 		T.TransactionID, DateAcquired,
			AcquisitionPrice, WorkID,
			PL.AskingPrice AS PriceListAskingPrice
FROM 		TRANS T, PRICELIST PL
WHERE		T.TransactionID = PL.TransactionID
	 AND	T.TransactionID = 255;
     
     
     
SELECT * FROM PRICELIST;
