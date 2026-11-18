from taskmanager.lookup import find_task


def complete_task(tasks, task_id):
    """Mark one task as completed."""
    task = find_task(tasks, task_id)
    if task is None:
        raise ValueError(f"No task found with id {task_id}.")
    task.completed = True
    return task