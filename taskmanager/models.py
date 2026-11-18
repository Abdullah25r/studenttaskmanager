from dataclasses import dataclass


@dataclass
class Task:
    """A single to-do item."""

    id: int
    title: str
    completed: bool = False