import sqlite3

def init_db(): # create a database
    conn = sqlite3.connect("tasks.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT,
                completed INTEGER DEFAULT 0
                )""")

    conn.commit()

def get_conn(): # returns conn, helper function for others
    return sqlite3.connect("tasks.db")

def add_task(tasks): # adds task to db
    if not tasks:
        return
    conn = get_conn()
    for task in tasks:
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
    conn.commit()

def del_task(task_ids): # deletes task from db, given the id of the task
    conn = get_conn()
    for task_id in task_ids:
        conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

def get_task(task_id): # returns a task given the id
    conn = get_conn()
    return conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()

def get_all_tasks(): # returns all tasks
    conn = get_conn()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    if not tasks:
        return
    return tasks

def complete_task(task_ids): # sets given task to completed (1)
    conn = get_conn()
    for task_id in task_ids:
        conn.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()

def toggle_task(task_ids): # toggles completion status of task (0 or 1)
    conn = get_conn()
    for task_id in task_ids:
        conn.execute("UPDATE tasks SET completed=1-completed WHERE id=?", (task_id,))
    conn.commit()

def drop(_):
    conn = sqlite3.connect("tasks.db")
    conn.execute("DROP TABLE tasks")
    conn.commit()
    return

def main(): # deletes the table, ONLY FOR DEBUG.
    drop(0)

if __name__ == "__main__":
    main()