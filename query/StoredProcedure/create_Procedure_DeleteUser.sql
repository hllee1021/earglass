-- USER 회원가입

DELIMITER //

CREATE PROCEDURE InsertNewUser
            (IN newID               Varchar(45),
             IN newPassword         Varchar(45),
             IN newName             Varchar(45),
             IN newBirth            Varchar(8),
             IN newPhoneNumber     Varchar(13),
             IN newGender           Varchar(1),
             IN newAddress          Varchar(100),
             IN newFK_TypeName      Varchar(45))

checkdupli:BEGIN

    DECLARE varRowCount     Varchar(45);
    DECLARE varFK_TypeName  Varchar(45);

    -- check to see if newID exist in database
    SELECT COUNT(*) INTO varRowCount
    FROM USER
    WHERE id = newID;


    -- if (varRowCount > 0) then ID already exits.
    IF (varRowCount > 0) THEN
        -- Print message
        SELECT 'User ID already exists.'
            AS InsertNewUserErrorMessage;
            ROLLBACK;
        LEAVE checkdupli;
    END IF;

	-- if (varRowCount = 0) then task does not exist in database.
    IF (varRowCount = 0) THEN
        -- Insert new User data.
	    INSERT INTO USER (id, Password, Name, BirthDate, PhoneNum, Gender, Address, FK_UserTypeName)
           VALUES(newID, newPassword,
		  		  newName, newBirth, newPhoneNumber, newGender, newAddress, newFK_TypeName);

        SELECT 'Insert new User successfully'
            AS InsertNewUserSuccessMessage;

    END IF;
-- END checkdupli
END checkdupli
//

DELIMITER ;
