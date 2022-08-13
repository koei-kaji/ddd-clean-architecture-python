from __future__ import annotations

from pydantic import BaseModel, StrictStr

from custom_pydantic.config import BaseFrozenConfig


class TaskName(BaseModel):
    value: StrictStr

    class Config(BaseFrozenConfig):
        ...
