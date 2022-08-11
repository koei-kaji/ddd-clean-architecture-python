from pydantic import BaseModel, StrictStr

from .task_status import TaskStatus


class TaskData(BaseModel):
    id: StrictStr
    name: StrictStr
    status: TaskStatus
