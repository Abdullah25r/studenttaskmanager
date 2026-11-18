from taskmanager.models import Task


def next_id(tasks):
    return max((task.id for task in tasks), default=0) + 1


def add_task(tasks, title):
    """Reject empty titles, then create the task."""
    if title is None or not title.strip():
        raise ValueError("Task title cannot be empty.")
    task = Task(id=next_id(tasks), title=title)
    tasks.append(task)
    return task