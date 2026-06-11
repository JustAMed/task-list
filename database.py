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

def add_task(tasks):
    if not tasks:
        return
    conn = get_conn()
    for task in tasks:
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
    conn.commit()

def del_task(task_ids):
    conn = get_conn()
    for task_id in task_ids:
        conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

def get_task(task_id):
    conn = get_conn()
    return conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()

def get_all_tasks():
    conn = get_conn()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    if not tasks:
        return
    return tasks

def complete_task(task_ids):
    conn = get_conn()
    for task_id in task_ids:
        conn.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()

def main():
    conn = sqlite3.connect("tasks.db")
    conn.execute("DROP TABLE tasks")
    conn.commit()
    return

if __name__ == "__main__":
    main()