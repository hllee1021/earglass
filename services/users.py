from database.connection import connect


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
    elif user['Password'] != password:
        return False
    return True