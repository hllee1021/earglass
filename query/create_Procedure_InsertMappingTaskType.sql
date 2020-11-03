-- 관리자가 원본 데이터 타입 지정하면 mapping_task_type에 insert

DELIMITER //

CREATE PROCEDURE InsertMappingTaskType
            (IN varFK_TaskName          Varchar(45),
             IN varOriginDataTypeName   Varchar(45))

BEGIN

    DECLARE     varFK_idORIGION_DATA_TYPE   Int(11);

    
    -- check to see if OriginDataTypeName exist in database
    IF NOT EXISTS(
        SELECT * FROM ORIGIN_DATA_TYPE
        WHERE   ORIGIN_DATA_TYPE.DataTypeName = varOriginDataTypeName)
        -- print message
        SELECT "invalid OriginDataTypeName"
        AS InsertMappingTaskTypeErrorMessage;)
    ELSE(

        )



END //


DELIMITER ;