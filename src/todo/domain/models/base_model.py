from pydantic import BaseModel

from custom_pydantic.config import BaseConfig, BaseFrozenConfig


class ValueObjectModel(BaseModel):
    class Config(BaseFrozenConfig):
        ...


class EntityModel(BaseModel):
    class Config(BaseConfig):
        ...
