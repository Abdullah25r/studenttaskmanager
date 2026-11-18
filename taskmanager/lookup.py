def find_task(tasks, task_id):
    """Return the task with this id, or None if it does not exist."""
    for task in tasks:
        if task.id == task_id:
            return task
    return None