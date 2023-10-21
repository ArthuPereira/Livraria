from contextlib import contextmanager
import pymysql.cursors

@contextmanager
def conect():
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        db = 'test',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )

    try:
        yield con
    finally:
        con.close()
