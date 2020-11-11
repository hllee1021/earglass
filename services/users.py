from database.connection import connect

# connect to db
connect = connect()
cursor = connect.cursor()

def get_user_by_id(id):
    # user 정보 받아오기
    cursor.execute("SELECT * FROM USER WHERE Id=%s", (id,))
    user = cursor.fetchone() 
    return user


def verify_user(id, password):
    # 유저 로그인 확인
    user = get_user_by_id(id)
    if not user:
        return False
    elif user["Password"] != password:
        return False
    return True


def sign_up(id, password, name, birth, phonenumber, gender, address, role):
    # 회원가입
    cursor.callproc('InsertNewUser', (id, password, name,
                                      birth, phonenumber, gender, address, role))
    message = cursor.fetchall()
    connect.commit()
    return message


def withdrawal():
    # 회원탈퇴?
    pass
