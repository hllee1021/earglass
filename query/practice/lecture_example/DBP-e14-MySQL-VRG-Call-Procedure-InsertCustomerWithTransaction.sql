/* *** SQL-CALL-CH10C-02 *** */

CALL InsertCustomerWithTransaction
    ('Gliddens', 'Melinda', 'Melinda.Gliddens@somewhere.com', '360', '765-8877',
	   'Sargent', 'Spanish Dancer', '588/750', 350.00);
       
/* *** SQL-Query-CH10C-06 *** */

SELECT * FROM CUSTOMER;