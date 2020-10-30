/* *** SQL-CALL-CH10C-01 *** */

CALL InsertCustomerAndInterests
    ('Bench', 'Michael', 'Michael.Bench@somewhere.com','206', '876-8822',  'French');
    
/* *** SQL-Query-View-CH10C-02 *** */

SELECT		* 
FROM 		CustomerInterestsView
ORDER BY	CustomerLastName, CustomerFirstName;