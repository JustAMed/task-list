import sqlite3

def init_db():
    conn = sqlite3.connect("tasks.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT,
                completed INTEGER DEFAULT 0
                )""")

    conn.commit()

def get_conn():
    return sqlite3.connect("tasks.db")

def add_task(task):
    conn = get_conn()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
    conn.commit()

def del_task(task_id):
    conn = get_conn()
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

def get_task(task_id):
    conn = get_conn()
    return conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()

def get_all_tasks():
    conn = get_conn()
    return conn.execute("SELECT * FROM tasks").fetchall()