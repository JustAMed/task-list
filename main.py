import database
import json
from parser import parse

def export(fname):
    result = []
    tasks = database.get_all_tasks()
    for idd, title, completed in tasks:
        result.append(
            {
                "id": idd,
                "title": title,
                "completed": completed
            }
        )
    with open(fname[0], "w") as f:
        json.dump(result, f, indent=4)
    return

def import_from_file(fname):
    try:
        with open(fname[0], "r") as f:
            tasks = json.load(f)
    except:
        print("No such file")
        return
    for task in tasks:
        database.add_task([task["title"]])
        if task["completed"] == 1:
            database.toggle_task([task["id"]])
    

task_actions = { # defines task: associated function
        "add": database.add_task,
        "del": database.del_task,
        "list": lambda args: render_table(database.get_all_tasks()), # ignores passing of args as function does not take arguments
        "complete": database.complete_task,
        "toggle": database.toggle_task,
    }

backup_actions = {
    "import": import_from_file,
    "export": export
}

families = {
        "task": task_actions,
        "backup": backup_actions
    }

def main():
    database.init_db() 
    while True:
        command = input("> ") 
        parsed = parse(command)
        if command in ["exit", "quit"]:
            return
        
        try: # get family, if fails then continue
            family = families[parsed["family"]]
        except KeyError:
            print("unknown family")
            continue

        family.get(parsed["action"], lambda x: print("unknown"))(parsed["args"]) # Run the associated function in actions dict. If no such action exists, print "unknown"

def render_table(tasks): # renders the table for action "list"
    if not tasks: 
        print("Nothing to see here.")
        return
    for id, title, completed in tasks: # Prints each task in format: id. title [✓/✗]
        status = "✓" if completed else "✗"
        print(f"{id}. {title} [{status}]")

if __name__ == "__main__":
    main()