-- -----------------------------------------------------
-- INSERT data for USERTYPE
-- -----------------------------------------------------
INSERT INTO USERTYPE VALUES ('평가자');
INSERT INTO USERTYPE VALUES ('제출자');
INSERT INTO USERTYPE VALUES ('관리자');


-- -----------------------------------------------------
-- INSERT data for USER
-- -----------------------------------------------------

ALTER TABLE USER AUTO_INCREMENT = 0;

INSERT INTO USER
	(Id, Password, Name, Gender, Birth, Phonenumber, FK_TypeName)
	VALUES ('manager', 'manager0000', '관리자', 'M', '00000000', '000-0000-0000', '관리자');

INSERT INTO USER
	(Id, Password, Name, Address, Gender, Birth, Phonenumber, FK_TypeName)
	VALUES ('hwayoung', 'hwayoung12345', '이화영', '서울특별시 서대문구 연세로 50', 'W', '19980327', '010-1243-5687', '제출자');

INSERT INTO USER
	(Id, Password, Name, Address, Gender, Birth, Phonenumber, FK_TypeName)
	VALUES ('yeonsoo', 'yeonsoo09876', '노연수', '서울특별시 서대문구 연세로 50', 'W', '19980327', '010-3238-1938', '제출자');

INSERT INTO USER
	(Id, Password, Name, Address, Gender, Birth, Phonenumber, FK_TypeName)
	VALUES ('coldbrew', '00coffee00', '나커피', '서울특별시 서대문구 연희로 17', 'M', '20000109', '010-3489-2833', '제출자');


INSERT INTO USER
	(Id, Password, Name, Address, Gender, Birth, Phonenumber, FK_TypeName)
	VALUES ('hwa4242', 'hwa424212345', '화사이', '서울특별시 마포구 망원로 3', 'M', '19930220', '010-7245-3246', '평가자');

INSERT INTO USER
	(Id, Password, Name, Address, Gender,  Birth, Phonenumber, FK_TypeName)
	VALUES ('soo9494', 'soo949412345', '수구사', '서울특별시 서대문구 연희로 9', 'W', '19870205', '010-8764-2394', '평가자');

INSERT INTO USER
	(Id, Password, Name, Address, Gender, Birth, Phonenumber, FK_TypeName)
	VALUES ('cold1004', 'cold100412345', '콜드천사', '서울특별시 서대문구 연세로 50', 'W', '20021224', '010-2354-6452', '평가자');



-- -----------------------------------------------------
-- INSERT data for TASK
-- -----------------------------------------------------
INSERT INTO TASK
	(TaskName, Description, MinPeriod, FK_IdManager)
	VALUES ('생활코딩-자바스크립트 제 1강 자막01', '생활코딩 YouTube 영상에 자막을 만들어주세요.', 4, 1);

INSERT INTO PARTICIPATION
    (FK_TaskName, FK_idUSER)
    VALUES ('생활코딩-자바스크립트 제 1강 자막01', 2);

INSERT INTO PARTICIPATION
    (FK_TaskName, FK_idUSER)
    VALUES ('생활코딩-자바스크립트 제 1강 자막01', 7);


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
    VALUES ('database/originDSF/srt/스타워즈 에피소드 II 클론의 습격 Star.Wars.Episode.II.Attack.of.the.Clones.2002.REMASTERED.1080p.10bit.BluRay.8CH.x265.HEVC-PSA.2audio[Kor+Eng].Korean.srt',1,'2020-10-29 02:55:05', '생활코딩-자바스크립트 제 1강 자막01', 2, 2);

INSERT INTO ORIGIN_DSF
    (OriginFile, SubmitNum, Date, FK_TaskName, FK_idMAPPING_TASK_TYPE, FK_idUSER)
    VALUES ('database/originDSF/smi/BBC 인류의 기원walking with cavemen e02 what a whopper.Korean.smi',2,'2020-10-29 08:35:55', '생활코딩-자바스크립트 제 1강 자막01', 1, 2);

INSERT INTO ORIGIN_DSF
    (OriginFile, SubmitNum, Date, FK_TaskName, FK_idMAPPING_TASK_TYPE, FK_idUSER)
    VALUES ('database/originDSF/smi/Joseph.King.of.Dreams.2000.1080p.BluRay.H264.AAC-JosephLee.Korean.smi',1,'2020-10-30 14:29:30', '생활코딩-자바스크립트 제 1강 자막01', 1, 7);


-- -----------------------------------------------------
-- INSERT data for PARSING_DSF
-- -----------------------------------------------------

ALTER TABLE PARSING_DSF AUTO_INCREMENT = 0;

INSERT INTO PARSING_DSF
	(ParsingFile, SubmitNum, NumRow, DuplicateRow, NullSubtitles, NullStartTime, NullEndTime, NullDuration,
	 NumLongValue, NumLongDuration, NumShortDuration, FK_idORIGIN_DSF, SystemScore, Pass, idUSER)
	VALUES ('url/hwayoung.csv', 1, 5, 0, 0, 0, 0, 0, 1, 0, 0, 1, 90, 0, 3);

INSERT INTO PARSING_DSF
	(ParsingFile, SubmitNum, NumRow, DuplicateRow, NullSubtitles, NullStartTime, NullEndTime, NullDuration,
	 NumLongValue, NumLongDuration, NumShortDuration, FK_idORIGIN_DSF, SystemScore, Pass, idUSER)
	VALUES ('url/hwayoung_2.csv', 2, 5, 2, 0, 0, 0, 0.1, 0, 0, 0, 2, 85, 0, 4);

INSERT INTO PARSING_DSF
	(ParsingFile, SubmitNum, NumRow, DuplicateRow, NullSubtitles, NullStartTime, NullEndTime, NullDuration,
	 NumLongValue, NumLongDuration, NumShortDuration, FK_idORIGIN_DSF, SystemScore, Pass, idUSER)
	VALUES ('url_/yeonsoo.csv', 1, 6, 0, 0, 0, 0, 0, 0, 0, 1, 3, 92, 0, 5);
/*

-- -----------------------------------------------------
-- INSERT data for EVALUATION
-- -----------------------------------------------------
INSERT INTO EVALUATION
	(idEVALUATION, FK_idPARSING_DSF, FK_idUSER, Score, Pass, StartTime, EndTime, Deadline, Status)
	VALUES ();

-- -----------------------------------------------------
-- INSERT data for TASK_DATA
-- -----------------------------------------------------
INSERT INTO TASK_DATA
	(FK_TaskName, StartTime, EndTime, Caption, PartNum, FK_idPARSING_DSF, idUSER)
	VALUES ('생활코딩-자바스크립트 제 1강 자막01', '00:00:00,000', '00:00:09,123', '연수야 안녕', 1, 2, 2);

INSERT INTO TASK_DATA
	(FK_TaskName, StartTime, EndTime, Caption, PartNum, FK_idPARSING_DSF, idUSER)
	VALUES ('생활코딩-자바스크립트 제 1강 자막01', '00:00:10,000', '00:00:16,392', '반가워', 1, 2, 2);

INSERT INTO TASK_DATA
	(FK_TaskName, StartTime, EndTime, Caption, PartNum, FK_idPARSING_DSF, idUSER)
	VALUES ('생활코딩-자바스크립트 제 1강 자막01', '00:00:17,392', '00:00:28,312', '오늘 뭐해? 나랑 놀자', 1, 2, 2);

INSERT INTO TASK_DATA
	(FK_TaskName, StartTime, EndTime, Caption, PartNum, FK_idPARSING_DSF, idUSER)
	VALUES ('생활코딩-자바스크립트 제 1강 자막01', '00:00:35,203', '00:00:38,320', '싫어', 2, 2, 2);

INSERT INTO TASK_DATA
	(FK_TaskName, StartTime, EndTime, Caption, PartNum, FK_idPARSING_DSF, idUSER)
	VALUES ('생활코딩-자바스크립트 제 1강 자막01', '00:00:42,000', '00:00:45,000', '알겠어..', 2, 2, 2);

*/








