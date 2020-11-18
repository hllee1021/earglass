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
    conn = connect()
    cur = conn.cursor()

    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    return result


def queryall(sql, fmt=tuple()):
    # executes 1 query and fetches all
    conn = connect()
    cur = conn.cursor()

    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result
