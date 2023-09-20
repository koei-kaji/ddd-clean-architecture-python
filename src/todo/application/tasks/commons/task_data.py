from pydantic import StrictStr

from custom_pydantic.model import BaseFrozenModel


class TaskData(BaseFrozenModel):
    task_id: StrictStr
    name: StrictStr
    status: StrictStr
