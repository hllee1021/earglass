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

-- -----------------------------------------------------
-- INSERT data for ORIGIN_DATA_TYPE
-- -----------------------------------------------------


-- -----------------------------------------------------
-- INSERT data for MAPPING_TASK_TYPE
-- -----------------------------------------------------

-- -----------------------------------------------------
-- INSERT data for ORIGIN_DSF
-- -----------------------------------------------------


-- -----------------------------------------------------
-- INSERT data for PARSING_DSF
-- -----------------------------------------------------


-- -----------------------------------------------------
-- INSERT data for TASK_DATA
-- -----------------------------------------------------


-- -----------------------------------------------------
-- INSERT data for EVALUATION
-- -----------------------------------------------------








