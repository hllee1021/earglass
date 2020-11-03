-- 관리자가 task table에 정보 insert

DELIMITER //

CREATE PROCEDURE InsertNewTask
            (IN newTaskName         Varchar(45),
             IN newDescription      Varchar(45),
             IN newMinPeriod        Int(11),
             IN newFK_idManager     Int(11))

checkdupli:BEGIN
    
    DECLARE varRowCount     Int;
    DECLARE varIdManager Int;

    -- check to see if varTaskName exist in database
    SELECT COUNT(*) INTO varRowCount
    FROM TASK
    WHERE TaskName = newTaskName;


    -- if (varRowCount > 0) then task already exits.
    IF (varRowCount > 0) THEN
        -- Print message
        SELECT 'Task name already exists.';
            ROLLBACK;
        LEAVE checkdupli;
    END IF;

	-- if (varRowCount = 0) then task does not exist in database.
    IF (varRowCount = 0) THEN
    inserttask:BEGIN
	    -- Rollback everything if unable to complete it.
	    START TRANSACTION;

        -- get idUSER surrogate key value, check for validity.
        SELECT idUSER INTO varIdManager
        FROM USER
        WHERE idUSER = newFK_idManager
            AND FK_TypeName = '관리자';
        
        IF (varIdManager IS NULL) THEN
        SELECT 'Invalid Manager ID';
		    ROLLBACK;
        LEAVE inserttask;    
 	      END IF;

        -- Insert new Customer data.
	    INSERT INTO TASK (TaskName, Description, MinPeriod, Status, FK_idManager)
           VALUES(newTaskName, newDescription,
		  		  newMinPeriod, 'ongoing', newFK_idManager);

        SELECT 'Insert new task successfully';

      -- END inserttask
    END inserttask;
    END IF;
-- END checkdupli
END checkdupli
//

DELIMITER ;
