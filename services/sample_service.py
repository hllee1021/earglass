from database.connection import queryall


def get_all():
    return queryall("SELECT * FROM SAMPLE")


def create():
    executeone("INSERT INTO SAMPLE VALUES ()", )
