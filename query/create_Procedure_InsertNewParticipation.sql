-- 제출자 참여시 Participation table에 insert / waiting

DELIMITER //

CREATE PROCEDURE InsertNewParticipation
            (IN     new_FK_TaskName         Varchar,
             IN     new_FK_idUSER           Int)

BEGIN

    INSERT INTO PARTICIPATION (FK_TaskName, FK_idUSER, status)
        VALUES(new_FK_TaskName, new_FK_idUSER, "waiting");

END
//

DELIMITER ;