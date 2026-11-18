from taskmanager.lookup import find_task


def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task:
        task.completed = True