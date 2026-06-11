from database import add_task, get_task, del_task, init_db, get_all_tasks

def main():
    init_db()
    while True:
        command = input("> ")
        words = command.split()
        if "add" in words:
            command = command.replace("add ", "", 1)
            add_task(command)
        if "list" in words:
            print(get_all_tasks())
        if "exit" in words:
            break

if __name__ == "__main__":
    main()