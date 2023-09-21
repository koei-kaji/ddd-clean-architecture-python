from pydantic import StrictStr

from ...base_request import BaseRequest
from ..commons.task_status import TaskStatus


class TaskPatchRequest(BaseRequest):
    name: StrictStr | None = None
    status: TaskStatus | None = None
