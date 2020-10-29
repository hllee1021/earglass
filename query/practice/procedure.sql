-- 제출자 참여시 Participation table에 insert / waiting

DELIMITER //

CREATE PROCEDURE InsertNewParticipation
            (IN     new_FK_TaskName         Varchar,
             IN     new_FK_idUSER           Int)

BEGIN

    DE