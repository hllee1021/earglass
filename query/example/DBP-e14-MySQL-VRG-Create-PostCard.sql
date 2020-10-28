CREATE TABLE `postcards_temp` (
  `postcards_temp_id` int(11) NOT NULL AUTO_INCREMENT,
  `ArtistName` varchar(45) DEFAULT NULL,
  `WorkTitle` varchar(45) DEFAULT NULL,
  `PostcardSize` varchar(12) DEFAULT NULL,
  `PostcardPrice` decimal(12,2) DEFAULT NULL,
  `QuantityOnHand` int(11) NOT NULL,
  `QuantityOnOrder` int(11) NOT NULL,
  `ArtistLastName` char(25) DEFAULT NULL,
  `ArtistID` int(11) DEFAULT NULL,
  PRIMARY KEY (`postcards_temp_id`),
  KEY `QuantityOnHand_index` (`QuantityOnHand`),
  KEY `QuantityOnOrder_index` (`QuantityOnOrder`))