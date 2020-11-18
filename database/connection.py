import pymysql
import sys

from database import config
config = config.config

# PyMySQL Documentation: https://pymysql.readthedocs.io/en/latest/index.html


def connect():
    connection = pymysql.connect(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        database=config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return connection


def queryone(sql, fmt=tuple()):
    # executes 1 query and fetches one
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, fmt)
        return cur.fetchone()
    except Exception as e:
        print(e)
        raise e
    finally:
        cur.close()
        conn.close()


def queryall(sql, fmt=tuple()):
    # executes 1 query and fetches all
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, fmt)
        return cur.fetchall()
    except Exception as e:
        print(e)
        raise e
    finally:
        cur.close()
        conn.close()

def execute(sql, fmt=tuple()):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, fmt)
        conn.commit()
    except Exception as e:
        print(e)
        raise e
    finally:
        cur.close()
        conn.close()

def callproc(sql, fmt=tuple()):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.callproc(sql, fmt)
        message = cur.fetchall()
        conn.commit()
        return message
    except Exception as e:
        print(e)
        raise e
    finally:
        cur.close()
        conn.close()