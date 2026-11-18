from taskmanager.lookup import find_task


def delete_task(tasks, task_id):
    """Delete a task by a valid id and return the removed task."""
    if not isinstance(task_id, int) or task_id < 1:
        raise ValueError("Task id must be a positive whole number.")
    task = find_task(tasks, task_id)
    if task is None:
        raise ValueError(f"No task found with id {task_id}.")
    tasks.remove(task)
    return task