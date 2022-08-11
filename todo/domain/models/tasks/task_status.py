from enum import Enum, unique


@unique
class TaskStatus(str, Enum):
    TODO = "todo"
    DONE = "done"
