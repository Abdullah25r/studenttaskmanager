from taskmanager.add import add_task
from taskmanager.complete import complete_task
from taskmanager.delete import delete_task
from taskmanager.display import format_tasks

MENU = """
Student Task Manager
1. Add task
2. Show tasks
3. Complete task(s)
4. Delete task
5. Quit
"""


def parse_id(text):
    try:
        return int(text.strip())
    except ValueError:
        raise ValueError("Task id must be a whole number.")


def handle_add(tasks):
    title = input("Task title: ")
    try:
        task = add_task(tasks, title)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Added task {task.id}: {task.title}")


def handle_show(tasks):
    print(format_tasks(tasks))


def handle_complete(tasks):
    raw = input("Task id(s) to complete (comma separated): ")
    for part in raw.split(","):
        try:
            complete_task(tasks, parse_id(part))
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"Completed task {part.strip()}.")


def handle_delete(tasks):
    raw = input("Task id to delete: ")
    try:
        delete_task(tasks, parse_id(raw))
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Deleted task {raw.strip()}.")


def run():
    tasks = []
    actions = {
        "1": handle_add,
        "2": handle_show,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option.")
        else:
            action(tasks)