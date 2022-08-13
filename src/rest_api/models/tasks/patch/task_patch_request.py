from pydantic import StrictStr

from ...base_request import BaseRequest
from ..commons.task_status import TaskStatus


class TaskPatchRequest(BaseRequest):
    id: StrictStr
    name: StrictStr | None = None
    status: TaskStatus | None = None
