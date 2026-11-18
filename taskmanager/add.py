from taskmanager.models import Task


def next_id(tasks):
    return max((task.id for task in tasks), default=0) + 1


def add_task(tasks, title):
    task = Task(id=next_id(tasks), title=title)
    tasks.append(task)
    return task