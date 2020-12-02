-- OriginDSF가 Pass하면 ParsingDSF로 저장

DELIMITER //

CREATE PROCEDURE InsertParsingDSF
            (IN newTaskName                 Varchar(45),
             IN newParsingFile              Longtext,
             IN newOriginDataTypeID         Varchar(45),
             IN newSubmitterID              Int(11),
             IN newPeriod                   Varchar(45),
             IN newFK_idORIGIN_DSF          Int(11),
             IN newRound                    Int(11),
             IN newSystemScore              Float)

checkexist:BEGIN

    DECLARE varidORIGIN_DSF Int(11);
    DECLARE varSubmitNum    Int(11);

    -- check if origin_dsf exists
    SELECT COUNT(*) INTO varidORIGIN_DSF
    FROM ORIGIN_DSF
    WHERE idORIGIN_DSF = newFK_idORIGIN_DSF;

    IF varidORIGIN_DSF = 0 
    THEN SELECT 'Origin DSF does not exist'
            AS OriginDSFErrorMessage;
            ROLLBACK;
        Leave checkexist;
    END IF;

    SELECT COUNT(*) INTO varSubmitNum
    FROM PARSING_DSF
    WHERE TaskName = newTaskName AND SubmitterID = newSubmitterID;

    IF (varSubmitNum = 0) THEN
        INSERT INTO PARSING_DSF (TaskName, ParsingFile, OriginDataTypeID, SubmitterID, SubmitNum, Period, TotalStatus, FK_idORIGIN_DSF, Round, SystemScore)
        VALUES (newTaskName, newParsingFile, newOriginDataTypeID, newSubmitterID, 1, newPeriod, 'ongoing', newFK_idORIGIN_DSF, newRound, newSystemScore);
        SELECT LAST_INSERT_ID();
    ELSE
        INSERT INTO PARSING_DSF (TaskName, ParsingFile, OriginDataTypeID, SubmitterID, SubmitNum, Period, TotalStatus, FK_idORIGIN_DSF, Round, SystemScore)
        VALUES (newTaskName, newParsingFile, newOriginDataTypeID, newSubmitterID, varSubmitNum+1, newPeriod, 'ongoing', newFK_idORIGIN_DSF, newRound, newSystemScore);
        SELECT LAST_INSERT_ID();
    END IF;

-- END checkexist
END checkexist
//

DELIMITER ;
