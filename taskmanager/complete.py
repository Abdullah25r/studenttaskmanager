from taskmanager.lookup import find_task


def complete_task(tasks, task_id):
    """Mark one task as completed."""
    task = find_task(tasks, task_id)
    if task is None:
        raise ValueError(f"No task found with id {task_id}.")
    if task.completed:
        raise ValueError(f"Task {task_id} is already completed.")
    task.completed = True
    return task


def complete_tasks(tasks, task_ids):
    """Complete several tasks. Returns (completed_tasks, error_messages)."""
    completed, errors = [], []
    for task_id in task_ids:
        try:
            completed.append(complete_task(tasks, task_id))
        except ValueError as error:
            errors.append(str(error))
    return completed, errors