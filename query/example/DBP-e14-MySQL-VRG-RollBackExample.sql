START TRANSACTION;

UPDATE customer
	SET	City = 'New York City'
    WHERE CustomerID = 1000;

UPDATE customer
	SET	City = 'New York City';

DELETE FROM customer_artist_int;

SELECT * FROM customer_artist_int;

ROLLBACK;