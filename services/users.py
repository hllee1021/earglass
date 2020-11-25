from database.connection import *

def get_user_by_index(user_index):
    return queryone("SELECT * FROM USER WHERE idUSER=%s", (user_index,))

def get_user_by_id(user_id):
    '''user 정보 받아오기'''
    return queryone("SELECT * FROM USER WHERE Id=%s", (user_id,))


def verify_user(user_id, password):
    '''유저 로그인 확인'''
    user = get_user_by_id(user_id)
    if not user:
        return False
    elif user["Password"] != password:
        return False
    return True


def sign_up(user_id, password, name, birth, phonenumber, gender, address, role):
    # 회원가입
    return callproc('InsertNewUser', (user_id, password, name,
                                      birth, phonenumber, gender, address, role))


def withdrawal():
    # 회원탈퇴?
    pass
