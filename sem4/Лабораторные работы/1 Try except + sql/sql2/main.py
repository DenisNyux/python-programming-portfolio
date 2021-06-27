import sqlite3


# Рефакторинг добавления данных (insert_param_data)
# Добавить код, который реализует:
# параметризованное удаление данных (DELETE),
# обновление (изменение) данных (UPDATE),
# выборку (извлечение) данных из таблицы stocks (SELECT)
# Добавить обработку исключительных ситуаций

def connect_to_db(path_to_db):
    connection = None
    if (path_to_db):
        try:
            # connection = sqlite3.connect(
            # 'file:' + path_to_db + '?mode=rw', uri=True)
            connection = sqlite3.connect(path_to_db)
        except:
            return None
        else:
            c = connection.cursor()
            return {"conn": connection, "cursor": c}
    return connection


def create_table(domens_lst, conn_dict):
    if isinstance(conn_dict, type(None)):
        raise sqlite3.OperationalError
    else:
        cu = conn_dict["cursor"]
        try:
            # Create table
            cu.execute(
                f"CREATE TABLE if not exists stocks ({domens_lst[0]} text, {domens_lst[1]} text, {domens_lst[2]} text,"
                f" {domens_lst[3]} real, {domens_lst[4]} int)")
        except sqlite3.OperationalError:
            print('tb already exists.')


def insert_param_data(conn, table_name, values):
    # date text, trans text, symbol text, qty real, price real
    c = conn.cursor()
    c.executemany(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)', values)
    conn.commit()


def show_data(table_name, conn):
    cur = conn.cursor()
    for record in cur.execute(f"SELECT * FROM {table_name}"):
        print(record)


def update_data(conn, table_name, domens):
    cur = conn.cursor()
    cur.execute(f'UPDATE {table_name} SET {domens[4]} = {domens[4]} + 1;')
    conn.commit()

def delete_last(conn, table_name, domens):
    cur = conn.cursor()
    cur.execute(f'DELETE FROM {table_name} WHERE id = MAX()')

# Config
table_name = 'stocks'
values = [('2020-02-20', 'BUY', 'APL', 22.03, 2000)]
domens = ['date', 'trans', 'symbol', 'qty', 'year']

conn_dict = connect_to_db('example.db')
conn, cur = conn_dict["conn"], conn_dict["cursor"]
create_table(domens, conn_dict)
# insert_param_data(conn, table_name, values)
update_data(conn, table_name, domens)
show_data(table_name, conn)
conn.close()
conn, cur = None, None
