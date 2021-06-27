import sqlite3

db_name = 'example.db'
creater = "CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)"
recs = [
    "INSERT INTO stocks VALUES ('2007-01-05','BUY','PHAT',100,35.14)",
    "INSERT INTO stocks VALUES ('2006-01-05','SELL','PHAT',100,35.14)",
    "INSERT INTO stocks VALUES ('2005-01-05','SELL','PHAT',100,35.14)",
]
deleter = "DELETE FROM stocks WHERE trans='BUY'"
selector = "SELECT * FROM stocks"


def connect(name: str):
    if db_name != 'example.db':
        raise FileNotFoundError
    return sqlite3.connect(name)


def create_table(cursor, sql):
    try:
        cursor.execute(sql)
    except sqlite3.OperationalError:
        print('it already exists....')


def add_records(cursor, records: list):
    try:
        for i in range(0, len(records)):
            cursor.execute(records[i])

    except sqlite3.OperationalError:
        print('It can`t be added')


def print_table(cursor, sql):
    try:
        for record in cursor.execute(sql):
            print(record)
    except sqlite3.OperationalError:
        print('I can`t print it')


db = connect(db_name)
c = db.cursor()
create_table(c, creater)
add_records(c, recs)
print_table(c, selector)
db.close()
#
# def create_table(cursor, sql):
#     try:
#         cursor.execute(sql)
#         return cursor
#     except sqlite3.OperationalError:
#         print('it already exists....')
#
#
# def add_records(cursor, records: list):
#     try:
#         for i in range(0, len(records)):
#             cursor.execute(records)
#         return cursor
#     except sqlite3.OperationalError:
#         print('It can`t be added')
#
#
# def delete_records(cursor, sql):
#     try:
#         cursor.execute(sql)
#         return cursor
#     except sqlite3.OperationalError:
#         print('There is nothing to delete')
#
#
# def print_table(cursor, sql):
#     try:
#         for record in cursor.execute(sql):
#             print(record)
#     except sqlite3.OperationalError:
#         print('I can`t print it')
#


#
# try:
#     c.execute('''CREATE TABLE stocks
#                  (date text, trans text, symbol text, qty real, price real)''')
# except sqlite3.OperationalError:
#     print('it already exists....')
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','SELL','PHAT',100,35.14)")
# conn.commit()
# c.execute("DELETE FROM stocks WHERE trans='BUY'")
# qty = 300
# trans = 'SAS'
# symbol = 'PHAT'
# c.execute(f"UPDATE stocks SET trans = '{trans}', qty = {qty} WHERE symbol = '{symbol}'")
# # Printing
# for record in c.execute(("SELECT * FROM stocks")):
#     print(record)
