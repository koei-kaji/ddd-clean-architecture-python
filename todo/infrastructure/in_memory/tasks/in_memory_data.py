from typing import Dict, NamedTuple


class TaskTuple(NamedTuple):
    name: str
    status: str


data: Dict[str, TaskTuple] = {"dummy": TaskTuple(name="dummy task", status="todo")}
