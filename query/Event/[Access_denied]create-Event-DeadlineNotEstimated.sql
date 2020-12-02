CREATE EVENT DeadlineNotEstimated
    ON SCHEDULE
        EVERY 10 second
        STARTS '2019-01-01 00:00:00'
    DO
        UPDATE EVALUATION
            SET
                EndTime = NOW(),
                Status = 'notEstimated'
            WHERE Deadline > NOW();