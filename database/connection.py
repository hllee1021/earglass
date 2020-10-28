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
        database=config['database']
    )
    return connection

# executes 1 query and fetches one
def queryone(sql):
    conn = connect()
    cur = conn.cursor()

    cur.execute(sql)
    return cur.fetchone()

# executes 1 query and fetches all
def queryall(sql):
    conn = connect()
    cur = conn.cursor()

    cur.execute(sql)
    return cur.fetchall()
