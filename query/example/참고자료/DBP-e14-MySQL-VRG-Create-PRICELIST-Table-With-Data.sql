/********************************************************************************/
/*																		        */
/*	Kroenke and Auer - Database Processing (14th Edition) Chapter 10C         	*/
/*																		        */
/*	The View Ridge Gallery (VRG) - Create PRICELIST Table			            */
/*																		        */
/*	These are the MySQL 5.6 SQL code solutions                              	*/
/*																		        */
/********************************************************************************/

/* *** SQL-CREATE-TABLE-CH10C-01 *** */

CREATE TABLE PRICELIST (
		TransactionID	Int						NOT NULL,
		AskingPrice		Numeric(8,2)			NOT NULL,
		CONSTRAINT		PriceListPK			PRIMARY KEY(TransactionID),
		CONSTRAINT		TransPriceListFK	FOREIGN KEY(TransactionID)
                            REFERENCES TRANS(TransactionID)
                                      ON UPDATE NO ACTION
                                      ON DELETE NO ACTION
		);

/* *** SQL-INSERT-CH10C-03 *** */

INSERT INTO PRICELIST (TransactionID, AskingPrice)
		SELECT	TransactionID, AskingPrice
		FROM	TRANS;
        
/* *** SQL-Query-CH10C-07 *** */

SELECT * FROM PRICELIST;





