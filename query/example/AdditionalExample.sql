CREATE TABLE `artist_data` (
  `ArtistID` int(11) NOT NULL AUTO_INCREMENT,
  `LastName` char(25) NOT NULL,
  `FirstName` char(25) NOT NULL,
  `Nationality` char(30) DEFAULT NULL,
  `DateOfBirth` decimal(4,0) DEFAULT NULL,
  `DateDeceased` decimal(4,0) DEFAULT NULL,
  PRIMARY KEY (`ArtistID`),
  UNIQUE KEY `ArtistAK1` (`LastName`,`FirstName`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

INSERT INTO ARTIST_DATA
	(LastName, FirstName, Nationality, DateOfBirth)
	SELECT LastName, FirstName, Nationality, DateOfBirth
	FROM 	ARTIST;

insert into ARTIST (LastName, FirstName, Nationality, DateOfBirth)
	select LastName, FirstName, Nationality, DateOfBirth
	from ARTIST_DATA
	on duplicate key update Nationality = values(Nationality);

SELECT	C.LastName, A.LastName
FROM	CUSTOMER AS C
			JOIN
			CUSTOMER_ARTIST_INT AS CI
			ON	C.CustomerID = CI.CustomerID
				JOIN ARTIST AS A 
					ON CI.ArtistID = A.ArtistID;
