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
    insertuser:BEGIN
	    -- Rollback everything if unable to complete it.
	    START TRANSACTION;

	    -- check Gender validity.
	    IF (newGender != 'W' AND newGender != 'M') THEN
            SELECT 'Invalid Gender'
                AS InsertNewUserErrorMessage;
            ROLLBACK;
            LEAVE insertuser;
        END IF;

	    SELECT TypeName INTO varFK_TypeName
	    FROM USERTYPE
	    WHERE TypeName = newFK_TypeName;

        -- check TypeName validity.
	    IF (varFK_TypeName IS NULL) THEN
            SELECT 'Invalid User Type Name'
                AS InsertNewUserErrorMessage;
            ROLLBACK;
            LEAVE insertuser;
        END IF;

        -- Insert new User data.
	    INSERT INTO USER (id, Password, Name, Birth, PhoneNumber, Gender, Address, FK_TypeName)
           VALUES(newID, newPassword,
		  		  newName, newBirth, newPhoneNumber, newGender, newAddress, newFK_TypeName);

        SELECT 'Insert new User successfully'
            AS InsertNewUserSuccessMessage;

      -- END insertuser
    END insertuser;
    END IF;
-- END checkdupli
END checkdupli
//

DELIMITER ;
