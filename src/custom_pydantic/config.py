from typing import Literal

from pydantic.config import BaseConfig as PydanticBaseConfig


class ABCConfig(PydanticBaseConfig):
    validate_all: bool = True
    validate_assignment = True
    copy_on_model_validation: Literal["none", "deep", "shallow"] = "deep"


class BaseConfig(PydanticBaseConfig):
    validate_all = True
    validate_assignment = True
    copy_on_model_validation: Literal["none", "deep", "shallow"] = "deep"


class BaseFrozenConfig(PydanticBaseConfig):
    validate_all: bool = True
    allow_mutation: bool = False
    copy_on_model_validation: Literal["none", "deep", "shallow"] = "deep"
