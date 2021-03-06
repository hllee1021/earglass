﻿-- MySQL Script generated by MySQL Workbench
-- Wed Nov 18 21:39:06 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema earglass
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema earglass
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `earglass` DEFAULT CHARACTER SET utf8 ;
USE `earglass` ;

-- -----------------------------------------------------
-- Table `earglass`.`USERTYPE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`USERTYPE` (
  `UserTypeName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`UserTypeName`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `earglass`.`USER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`USER` (
  `idUSER` INT NOT NULL AUTO_INCREMENT,
  `Id` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Gender` VARCHAR(1) NOT NULL,
  `BirthDate` VARCHAR(8) NOT NULL,
  `PhoneNum` VARCHAR(13) NOT NULL,
  `Address` VARCHAR(100) NULL,
  `UserScore` FLOAT NULL DEFAULT 0,
  `FK_UserTypeName` VARCHAR(45) NOT NULL,
  INDEX `FK_UserTypeName_idx` (`FK_UserTypeName` ASC),
  UNIQUE INDEX `PhoneNum_UNIQUE` (`PhoneNum` ASC),
  UNIQUE INDEX `Id_UNIQUE` (`Id` ASC),
  UNIQUE INDEX `idUSER_UNIQUE` (`idUSER` ASC),
  PRIMARY KEY (`idUSER`),
  CONSTRAINT `fk_USER_has_USERTYPE`
    FOREIGN KEY (`FK_UserTypeName`)
    REFERENCES `earglass`.`USERTYPE` (`UserTypeName`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `earglass`.`TASK`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`TASK` (
  `TaskName` VARCHAR(45) NOT NULL,
  `Description` TEXT(1000) NOT NULL,
  `MinPeriod` INT NOT NULL DEFAULT 0,
  `Status` VARCHAR(45) NOT NULL DEFAULT 'ongoing',
  `TaskDataTableName` VARCHAR(100) NOT NULL,
  `TaskDataTableSchemaInfo` TEXT(1000) NULL,
  `TaskDataTableLocation` TEXT(1000) NULL,
  `Deadline` DATETIME NULL,
  `FK_idManager` INT NOT NULL,
  `MaxDuplicatedRowRatio` FLOAT NOT NULL,
  `MaxNullRatoPerColumn` FLOAT NOT NULL,
  `PassCriteria` TEXT(1000) NOT NULL,
  INDEX `FK_idManager_idx` (`FK_idManager` ASC),
  PRIMARY KEY (`TaskName`),
  CONSTRAINT `fk_TASK_has_USER`
    FOREIGN KEY (`FK_idManager`)
    REFERENCES `earglass`.`USER` (`idUSER`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `earglass`.`PARTICIPATION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`PARTICIPATION` (
  `FK_TaskName` VARCHAR(45) NOT NULL,
  `FK_idUSER` INT NOT NULL,
  `Status` VARCHAR(45) NULL,
  `Comment` TEXT(1000) NULL,
  PRIMARY KEY (`FK_TaskName`, `FK_idUSER`),
  INDEX `FK_idUSER_idx` (`FK_idUSER` ASC),
  INDEX `FK_idTaskName_idx` (`FK_TaskName` ASC),
  CONSTRAINT `fk_PARTICIPATION_has_TASK`
    FOREIGN KEY (`FK_TaskName`)
    REFERENCES `earglass`.`TASK` (`TaskName`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_PARTICIPATION_has_USER`
    FOREIGN KEY (`FK_idUSER`)
    REFERENCES `earglass`.`USER` (`idUSER`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `earglass`.`ORIGIN_DATA_TYPE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`ORIGIN_DATA_TYPE` (
  `idORIGIN_DATA_TYPE` INT NOT NULL AUTO_INCREMENT,
  `SchemaInfo` VARCHAR(1000) NULL,
  `MappingInfo` VARCHAR(1000) NOT NULL,
  `DataTypeName` JSON NULL,
  `TaskName` VARCHAR(45) NULL,
  PRIMARY KEY (`idORIGIN_DATA_TYPE`),
  INDEX `fk_ORIGIN_DATA_TYPE_TASK1_idx` (`TaskName` ASC),
  CONSTRAINT `fk_ORIGIN_DATA_TYPE_TASK1`
    FOREIGN KEY (`TaskName`)
    REFERENCES `earglass`.`TASK` (`TaskName`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `earglass`.`ORIGIN_DSF`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`ORIGIN_DSF` (
  `idORIGIN_DSF` INT NOT NULL AUTO_INCREMENT,
  `OriginFile` LONGTEXT NOT NULL,
  `SummitNum` INT NOT NULL DEFAULT 0,
  `DateTime` DATETIME NOT NULL,
  `Period` VARCHAR(45) NOT NULL,
  `Round` INT NOT NULL,
  `FK_TaskName` VARCHAR(45) NULL,
  `FK_idUSER` INT NULL,
  `FK_idORIGIN_DATA_TYPE` INT NULL,
  PRIMARY KEY (`idORIGIN_DSF`),
  UNIQUE INDEX `idORIGIN_DSF_UNIQUE` (`idORIGIN_DSF` ASC),
  INDEX `fk_ORIGIN_DSF_PARTICIPATION1_idx` (`FK_TaskName` ASC, `FK_idUSER` ASC),
  INDEX `fk_ORIGIN_DSF_ORIGIN_DATA_TYPE1_idx` (`FK_idORIGIN_DATA_TYPE` ASC),
  CONSTRAINT `fk_ORIGIN_DSF_has_PARTICIPATION`
    FOREIGN KEY (`FK_TaskName` , `FK_idUSER`)
    REFERENCES `earglass`.`PARTICIPATION` (`FK_TaskName` , `FK_idUSER`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_ORIGIN_DSF_ORIGIN_DATA_TYPE1`
    FOREIGN KEY (`FK_idORIGIN_DATA_TYPE`)
    REFERENCES `earglass`.`ORIGIN_DATA_TYPE` (`idORIGIN_DATA_TYPE`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `earglass`.`PARSING_DSF`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`PARSING_DSF` (
  `idPARSING_DSF` INT NOT NULL AUTO_INCREMENT,
  `TaskName` VARCHAR(45) NOT NULL,
  `ParsingFile` LONGTEXT NOT NULL,
  `OriginDataTypeID` VARCHAR(45) NULL,
  `SubmitterID` VARCHAR(45) NOT NULL,
  `SubmitNum` INT NOT NULL DEFAULT 0,
  `Period` VARCHAR(45) NULL,
  `Round` INT NOT NULL,
  `SystemScore` FLOAT NULL,
  `AverageScore` FLOAT NULL,
  `TotalScore` FLOAT NULL,
  `Pass` VARCHAR(45) NULL,
  `TotalStatus` VARCHAR(45) NULL,
  `FK_idORIGIN_DSF` INT NULL,
  PRIMARY KEY (`idPARSING_DSF`),
  UNIQUE INDEX `idPARSING_DSF_UNIQUE` (`idPARSING_DSF` ASC),
  INDEX `fk_PARSING_DSF_ORIGIN_DSF1_idx` (`FK_idORIGIN_DSF` ASC),
  CONSTRAINT `fk_PARSING_DSF_has_ORIGIN_DSF`
    FOREIGN KEY (`FK_idORIGIN_DSF`)
    REFERENCES `earglass`.`ORIGIN_DSF` (`idORIGIN_DSF`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `earglass`.`EVALUATION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `earglass`.`EVALUATION` (
  `idEVALUATION` INT NOT NULL,
  `FK_idPARSING_DSF` INT NOT NULL,
  `FK_idEstimator` INT NULL,
  `Score` INT NULL,
  `Pass` VARCHAR(45) NULL,
  `StartTime` VARCHAR(11) NOT NULL,
  `EndTime` VARCHAR(11) NULL,
  `Deadline` DATETIME NOT NULL,
  `Status` VARCHAR(45) NOT NULL DEFAULT 'ongoing',
  PRIMARY KEY (`idEVALUATION`),
  INDEX `fk_PARSING_DSF_has_USER_USER1_idx` (`FK_idEstimator` ASC),
  INDEX `fk_PARSING_DSF_has_USER_PARSING_DSF1_idx` (`FK_idPARSING_DSF` ASC),
  CONSTRAINT `fk_EVALUATION_has_PARSING_DSF`
    FOREIGN KEY (`FK_idPARSING_DSF`)
    REFERENCES `earglass`.`PARSING_DSF` (`idPARSING_DSF`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_EVALUATION_has_USER`
    FOREIGN KEY (`FK_idEstimator`)
    REFERENCES `earglass`.`USER` (`idUSER`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;