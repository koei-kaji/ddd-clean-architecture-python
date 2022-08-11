from pydantic import BaseModel, StrictStr

from custom_pydantic.config import BaseFrozenConfig


class TaskData(BaseModel):
    task_id: StrictStr
    name: StrictStr
    status: StrictStr

    class Config(BaseFrozenConfig):
        ...
