from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfig


class BaseRequest(BaseModel):
    class Config(BaseFrozenConfig):
        ...
