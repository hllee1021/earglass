-- 관리자가 task table에서 특정 row delete

DELIMITER //

CREATE PROCEDURE UpdateTaskStatus
            (IN currentTaskName     Varchar(45),
             IN newStatus           Varchar(45))

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
            AS UpdateTaskStatusErrorMessage;
            ROLLBACK;
        LEAVE checkrow;
    END IF;

	-- if (varRowCount > 0) then task exists in database.
    IF (varRowCount = 1) THEN
        IF newStatus IN ('ongoing', 'done', null) THEN
            UPDATE TASK
            SET Status = newStatus
            WHERE TaskName = currentTaskName;
        ELSE
            SELECT 'Invalid status value'
                AS UpdateTaskStatusErrorMessage;
            LEAVE checkrow;
        END IF;
        SELECT 'update task status successfully'
            AS UpdateTaskStatusSuccessMessage;

    END IF;

-- END checkrow
END checkrow
//

DELIMITER ;
