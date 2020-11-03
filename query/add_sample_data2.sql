INSERT INTO PARTICIPATION
    (FK_TaskName, FK_idUSER)
    VALUES ('생활코딩-자바스크립트 제 1강 자막01', 2);

INSERT INTO PARTICIPATION
    (FK_TaskName, FK_idUSER)
    VALUES ('생활코딩-자바스크립트 제 1강 자막01', 3);

-- -----------------------------------------------------
-- INSERT data for ORIGIN_DATA_TYPE
-- -----------------------------------------------------

ALTER TABLE ORIGIN_DATA_TYPE AUTO_INCREMENT = 0;

INSERT INTO ORIGIN_DATA_TYPE
    (DataTypeName,SchemaInfo, MappingInfo)
    VALUES ('SMI', '<SYNC Start=######><P CLASS=KRCC>Caption / <SYNC Start=######><P CLASS=KRCC>&nbsp;','StartTime:<SYNC Start=######> / EndTime:<SYNC Start=######><P CLASS=KRCC>&nbsp; / Caption:<P CLASS=KRCC>Caption');

INSERT INTO ORIGIN_DATA_TYPE
    (DataTypeName,SchemaInfo, MappingInfo)
    VALUES ('SRT', 'num / ##:##:##,### --> ##:##:##,### / Caption','StartTime:##:##:##,### / EndTime:--> ##:##:##,### / Caption:Caption');

INSERT INTO ORIGIN_DATA_TYPE
    (DataTypeName,SchemaInfo, MappingInfo)
    VALUES ('CSV', 'num / ##:##:##,### / ##:##:##,### / Caption','StartTime:##:##:##,### / EndTime:##:##:##,### / Caption:Caption');

-- -----------------------------------------------------
-- INSERT data for MAPPING_TASK_TYPE
-- -----------------------------------------------------

ALTER TABLE MAPPING_TASK_TYPE AUTO_INCREMENT = 0;

INSERT INTO MAPPING_TASK_TYPE
    (FK_TaskName, FK_IdORIGIN_DATA_TYPE)
    VALUES ('생활코딩-자바스크립트 제 1강 자막01', 1);

INSERT INTO MAPPING_TASK_TYPE
    (FK_TaskName, FK_IdORIGIN_DATA_TYPE)
    VALUES ('생활코딩-자바스크립트 제 1강 자막01', 2);

INSERT INTO MAPPING_TASK_TYPE
    (FK_TaskName, FK_IdORIGIN_DATA_TYPE)
    VALUES ('생활코딩-자바스크립트 제 1강 자막01', 3);

-- -----------------------------------------------------
-- INSERT data for ORIGIN_DSF
-- -----------------------------------------------------

ALTER TABLE ORIGIN_DSF AUTO_INCREMENT = 0;

INSERT INTO ORIGIN_DSF
    (OriginFile, SubmitNum, Date, FK_TaskName, FK_idMAPPING_TASK_TYPE, FK_idUSER)
    VALUES ('url\\yeonsoo.srt',1,'2020-10-29', '생활코딩-자바스크립트 제 1강 자막01', 1, 2);

INSERT INTO ORIGIN_DSF
    (OriginFile, SubmitNum, Date, FK_TaskName, FK_idMAPPING_TASK_TYPE, FK_idUSER)
    VALUES ('url\\yeonsoo.smi',2,'2020-10-29', '생활코딩-자바스크립트 제 1강 자막01', 2, 2);

INSERT INTO ORIGIN_DSF
    (OriginFile, SubmitNum, Date, FK_TaskName, FK_idMAPPING_TASK_TYPE, FK_idUSER)
    VALUES ('url\\yeonsoo.csv',1,'2020-10-29', '생활코딩-자바스크립트 제 1강 자막01', 2, 3);
