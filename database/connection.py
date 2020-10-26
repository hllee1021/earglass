import mariadb
import sys

from . import config
config = config.db_config

# mariadb-python driver documentation: https://mariadb-corporation.github.io/mariadb-connector-python/index.html

def connect():
    connection = mariadb.connect(
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
