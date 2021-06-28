import sqlite3
import functools


def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
      if inner.called:
        func(*args, **kwargs)
        inner.called = False
    return inner



def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            connection = sqlite3.connect(
                'file:' + path_to_db + '?mode=rw', uri=True)
            # connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}

    return connection


def logging(conn, table):
    login = str(input("Введите логин: "))
    password = str(input("Введите пароль: "))
    user_query = "SELECT * FROM " + str(table) + " WHERE pass=" + "'" + password + "'" "AND login="+ "'" + login + "'"
    cursor = conn.cursor()
    res = cursor.execute(user_query)
    user_info = res.fetchall()
    if (user_info and user_info[0][0] == login and user_info[0][1] == password):
        private_zone_area()
        # print(*user_info)
        return str(user_info[0][2])
    else:
        print("Пользователя с таким паролем или логином не существует")
        return False


def private_zone_area():
    print("private_zone_area")

    return "private_zone_area"


def get_users_from_table(conn, table):
    sql_query = "SELECT * FROM " + str(table)
    cursor = conn.cursor()
    res = cursor.execute(sql_query)
    users_lst = res.fetchall()

    print(users_lst)

    return users_lst

def add_users_create_table(cur, conn):
    try:
        sql_query = '''CREATE TABLE users
                 (login text, pass text, role int)'''
        cur.execute(sql_query)
    except sqlite3.OperationalError as e:
        e_str = str(e)
        if ("already exists" in e_str):
            print(f' NOTICE: {e}. CONTINUE ')
            sql_query = '''INSERT INTO users VALUES (?, ?, ?)'''
            users_lst = [('root', '123', 0), ('admin', '789', 1), ('user', 'qwe', 2)]
            try:
                cur.executemany(sql_query, users_lst)
                conn.commit()
            except sqlite3.Error as e:
                print(f'Error with adding users to db. {e}')


def check_privelegies(log):
    if log == '0':
        print('У вас права root')
    elif log == '1':
        print('У вас права admin')
    elif log == '2':
        print('У вас права user')




def main():
    once(connect_to_db)
    conn_dict = connect_to_db('example.db')
    conn, cur = conn_dict["conn"], conn_dict["cursor"]
    a = connect_to_db('example.db')
    # users = get_users_from_table(conn, 'users')
    # print(users)
    log = logging(conn, 'users')
    # print(log)
    while not(log):
        log = logging(conn, 'users')
    check_privelegies(log)
    conn.close()
    cur, conn = None, None

main()