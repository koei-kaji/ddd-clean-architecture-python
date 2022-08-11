from pydantic import StrictStr

from ...abc import ABCInputData
from ..commons.task_status import TaskStatus


class TaskUpdateInputData(ABCInputData):
    task_id: StrictStr
    name: StrictStr | None = None
    status: TaskStatus | None = None
