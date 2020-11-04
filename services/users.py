from database.connection import connect

connect = connect()
cursor = connect.cursor()

def get_user_by_id(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER WHERE Id=%s", (id,))
    user = cur.fetchone()
    return user


def verify_user(id, password):
    user = get_user_by_id(id)
    if not user:
        return False
    elif user["Password"] != password:
        return False
    return True

def sign_up(task_name, status):
    # 테스크 상태 업데이트
    cursor.callproc('InsertNewUser', (task_name, status))
    message = cursor.fetchall()
    connect.commit()
    return message
