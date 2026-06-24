import database
from parser import parse

actions = { # defines task: associated function
    "add": database.add_task,
    "del": database.del_task,
    "list": lambda args: render_table(database.get_all_tasks()), # ignores passing of args as function does not take arguments
    "complete": database.complete_task,
    "toggle": database.toggle_task,
}

families = {
    "task": actions
}

def main():
    database.init_db() 
    while True:
        command = input("> ") 
        parsed = parse(command)
        if command in ["exit", "quit":
            return
        actions.get(parsed["action"], lambda x: print("unknown"))(parsed["args"]) # Run the associated function in actions dict. If no such action exists, print "unknown"

def render_table(tasks): # renders the table for action "list"
    if not tasks: 
        print("Nothing to see here.")
        return
    for id, title, completed in tasks: # Prints each task in format: id. title [✓/✗]
        status = "✓" if completed else "✗"
        print(f"{id}. {title} [{status}]")

if __name__ == "__main__":
    main()