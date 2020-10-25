import mariadb
import sys

from . import config
config = config.db_config

def connect():
    connection = mariadb.connect(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        database=config['database']
    )
    return connection
