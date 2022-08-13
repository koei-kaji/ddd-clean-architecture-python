from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfig


class BaseResponse(BaseModel):
    class Config(BaseFrozenConfig):
        ...
