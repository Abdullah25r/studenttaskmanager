def format_tasks(tasks):
    """Return the task list as printable text."""
    if not tasks:
        return "No tasks yet."
    lines = []
    for task in tasks:
        mark = "x" if task.completed else " "
        lines.append(f"[{mark}] {task.id}. {task.title}")
    return "\n".join(lines)