from taskmanager.models import Task

MAX_TITLE_LENGTH = 100


def next_id(tasks):
    return max((task.id for task in tasks), default=0) + 1


def add_task(tasks, title):
    """Validate the title, create a task, and append it to the list."""
    if title is None or not title.strip():
        raise ValueError("Task title cannot be empty.")
    title = title.strip()
    if len(title) > MAX_TITLE_LENGTH:
        raise ValueError(f"Task title cannot exceed {MAX_TITLE_LENGTH} characters.")
    task = Task(id=next_id(tasks), title=title)
    tasks.append(task)
    return task