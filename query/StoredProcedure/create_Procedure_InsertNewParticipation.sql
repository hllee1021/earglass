-- 제출자 참여시 Participation table에 insert / waiting

DELIMITER //

CREATE PROCEDURE InsertNewParticipation
            (IN     newFK_TaskName         Varchar(45),
             IN     newFK_idUSER           Int(11))

checkexist: BEGIN
    IF EXISTS (SELECT * FROM PARTICIPATION
                WHERE FK_TaskName = newFK_TaskName
                AND FK_idUSER = newFK_idUSER) THEN
            SELECT 'already parcitipate'
            AS InsertNewParticipationErrorMessage;
            ROLLBACK;
        LEAVE checkexist;
    END IF;

    INSERT INTO PARTICIPATION (FK_TaskName, FK_idUSER, Status)
        VALUES(newFK_TaskName, newFK_idUSER, 'waiting');

END
//

DELIMITER ;