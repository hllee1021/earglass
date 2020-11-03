-- 관리자가 task table에서 특정 row의 정보 edit

DELIMITER //

CREATE PROCEDURE EditTask
            (IN currentTaskName     Varchar(45),
             IN newDescription      Text,
             IN newMinPeriod        Int(11))

checkrow:BEGIN
    
    DECLARE varRowCount     Int;

    -- check to see if currentTaskName exist in database
    SELECT COUNT(*) INTO varRowCount
    FROM TASK
    WHERE TaskName = currentTaskName;


    -- if (varRowCount = 0) then task does not exist in database.
    IF (varRowCount = 0) THEN
        -- Print message
        SELECT 'Task name does not exist.'
            AS EditTaskErrorMessage;
            ROLLBACK;
        LEAVE checkrow;
    END IF;

	-- if (varRowCount = 1) then task exists in database.
    IF (varRowCount = 1) THEN
        UPDATE TASK
        SET Description = newDescription, MinPeriod = newMinPeriod
        WHERE TaskName = currentTaskName;
        
        SELECT 'Edit task info successfully'
            AS EditTaskSuccessMessage;

    END IF;

-- END checkrow
END checkrow
//

DELIMITER ;
