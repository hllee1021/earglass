from database.connection import connect


def get_tasks(page):
    # 페이지 번호에 따른 task 리턴
    pass


def get_users(page):
    # 페이지 번호에 따른 user 리턴
    pass


def search_user(column, search_word, page):
    # column에 word로 검색한 결과를 page에 따라 리턴
    pass


def show_submitter(user_id):
    # Submitter 에 대한 상세 정보 열람
    pass


def show_estimator(user_id):
    # Estimator에 대한 상세 정보 열람
    pass


def add_task(data):
    # 테스크 생성
    pass


def remove_task(task_id):
    # 테스크 제거
    pass


def edit_task(task_id, data):
    # 테스크 수정
    pass


def show_estimate_status(user_id):
    # 평가자 평가파일 현황
    pass


def show_submit_status(user_id):
    # 제출자 제출 현황
    pass
