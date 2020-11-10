from database.connection import connect

connect = connect()
cursor = connect.cursor()

# user 정보 받아오기
def get_user_by_id(id):
    cursor.execute("SELECT Id, Password, Name, Gender, Address, Birth, PhoneNumber, FK_TypeName AS Role, UserScore FROM USER WHERE Id=%s", (id,))
    user = cursor.fetchone() 
    return user

# 유저 로그인 확인
def verify_user(id, password):
    user = get_user_by_id(id)
    if not user:
        return False
    elif user["Password"] != password:
        return False
    return True


# 회원가입
def sign_up(id, password, name, birth, phonenumber, gender, address, role):
    cursor.callproc('InsertNewUser', (id, password, name,
                                      birth, phonenumber, gender, address, role))
    message = cursor.fetchall()
    connect.commit()
    return message

# 회원탈퇴?
def withdrawal():
    pass
