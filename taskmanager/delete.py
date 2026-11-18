from taskmanager.lookup import find_task


def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task:
        tasks.remove(task)