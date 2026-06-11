import database
from parser import parse

actions = {
    "add": database.add_task,
    "del": database.del_task,
    "list": lambda args: render_table(database.get_all_tasks()),
    "complete": database.complete_task,
}

def main():
    database.init_db()
    while True:
        command = input("> ")
        action, args = parse(command)
        if action == "exit":
            return
        actions.get(action, lambda x: print("unknown"))(args)

def render_table(tasks):
    if not tasks:
        print("Nothing to see here.")
        return
    for id, title, completed in tasks:
        status = "✓" if completed else "✗"
        print(f"{id}. {title} [{status}]")

if __name__ == "__main__":
    main()