from database.connection import connect


def get_user_by_id(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT Id, Name, Gender, Address, Birth, PhoneNumber, FK_TypeName AS Role, UserScore FROM USER WHERE Id=%s", (id,))
    user = cur.fetchone()
    return user

def verify_user(id, password):
    user = get_user_by_id(id)
    if not user:
        return False
    elif user["Password"] != password:
        return False
    return True


def sign_up(id, password, name, birth, phonenumber, gender, address, role):
    # 테스크 상태 업데이트
    conn = connect()
    cur = conn.cursor()
    cur.callproc('InsertNewUser', (id, password, name,
                                      birth, phonenumber, gender, address, role))
    message = cur.fetchall()
    conn.commit()
    return message
