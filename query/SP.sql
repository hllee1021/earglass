-- 회원가입 시 user에 insert (user가 평가자일 때 score default는 50점)

DELIMITER //

CREATE PROCEDURE InsertNewUser
    (new_Id in varchar,
    new_Password in varchar,
    new_Name in varchar,
    new_Gender in varchar,
    new_Address in varchar,
    new_Birth in varchar,
    new_PhoneNumber in varchar,
    new_FK_TypeName in varchar)
IS
BEGIN
    INSERT INTO USER
        (Id, Password, Name, Gender, Address, Birth, Phonenumber, FK_TypeName)
        VALUES (new_Id, new_Password, new_Name, new_Gender, new_Address, new_Birth, new_PhoneNumber, new_FK_TypeName);
    if (new_FK_TypeName = '평가자')
    then
        INSERT INTO USER
            (UserScore)
            VALUES (50);
    else
        INSERT INTO USER
            (UserScore)
            VALUES (0);
    end if //

end //

-- 신상 정보 변경 시 업데이트

CREATE PROCEDURE UserInfoUpdate
    (temp_IdUSER in int,
    new_Password in varchar,
    new_Address in varchar,
    new_PhoneNumber in varchar)
IS
BEGIN
        UPDATE USER
            SET Password = new_Password,
                Address = new_Address,
                PhoneNumber = new_PhoneNumber
            WHERE idUser = temp_IdUSER;
    end //

-- 탈퇴 시 delete

CREATE PROCEduRE DeleteUser
    (temp_IdUSER in int)
IS
BEGIN
    DELETE FROM USER
        WHERE idUSER = temp_IdUSER;
end //

-- 평가 시작 시 평가 row insert

CREATE PROCEDURE InsertEvaluation
    (new_FK_idPARSING_DSF in int,
    new_FK_idUSER in int,
    new_StartTime in varchar,
    new_Deadline in datetime)
IS
BEGIN
    INSERT INTO EVALUATION
        (FK_idPARSING_DSF, FK_idUSER, StartTime, Deadline, Status)
        VALUES(new_FK_idPARSING_DSF, new_FK_idUSER, new_StartTime, new_Deadline, 'ongoing');
end //

-- 평가 완료 시 endtime, score, pass여부 insert / status 업데이트

CREATE PROCEDURE UpdateEvaluation
    (temp_idEVALUATION in int,
    new_EndTime in varchar,
    new_Score in int,
    new_Pass in varchar)
IS
BEGIN
    UPDATE EVALUATION
        SET EndTime = new_EndTime,
            Score = new_Score,
            Pass = new_Pass,
            Status = 'done'
        WHERE idEVALUATION = temp_idEVALUATION;
end //