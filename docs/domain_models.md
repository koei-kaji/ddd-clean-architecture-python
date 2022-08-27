# 1. Domain Models

In principle, the following rules apply.  

- Inherit [pydantic's BaseModel]
- Use [Strict Types]

## 1.1. Value Object

Inherit `custom_pydantic.config.BaseFrozenConfig` to be immutable.  

```python
from pydantic import BaseModel, StrictStr

from custom_pydantic.config import BaseFrozenConfig


class TaskId(BaseModel):
    value: StrictStr

    class Config(BaseFrozenConfig):
        ...
```

## 1.2. Entity

Inherit `custom_pydantic.config.BaseConfig`.  

```python
from pydantic import BaseModel

from custom_pydantic.config import BaseConfig

from .task_id import TaskId
from .task_name import TaskName


class Task(BaseModel):
    task_id: TaskId
    name: TaskName
    # other fields
    # ...

    class Config(BaseConfig):
        ...
    
    def change_name(self, name: TaskName) -> None:
        self.name = name

    # other methods
    # ...
```

## 1.3. Domain Service

Currently not implemented.  

## 1.4. Repository

1. Define the Repository's Interface class(ABC) in the `domain.models.<Entities>` module.  
2. Implement the concrete Repository class in the `infrastructure.<Infrastructure>.<Entities>` module.  

Methods of the Repository class take `Value Objects` or `Entities` as arguments and returns `Value Objects` or `Entities`.  

### 1.4.1. Example

- Interface class: [todo.domain.models.tasks.if_task_repository.py]
- Concrete class: [todo.infrastructure.in_memory.tasks.in_memory_task_repository.py]

## 1.5. Factory

1. Define the Factory's Interface class(ABC) in the `domain.models.<Entities>` module.  
2. Implement the concrete Factory class in the `infrastructure.<Infrastructure>.<Entities>` module.  

Methods of the Repository class take `Value Objects` as arguments and returns an `Entity`.  

### 1.5.1. Example

- Interface class: [todo.domain.models.tasks.if_task_factory.py]
- Concrete class: [todo.infrastructure.in_memory.tasks.in_memory_task_factory.py]

[pydantic's BaseModel]: https://pydantic-docs.helpmanual.io/usage/models/#basic-model-usage
[Strict Types]: https://pydantic-docs.helpmanual.io/usage/types/#strict-types

[todo.domain.models.tasks.if_task_repository.py]: ../src/todo/domain/models/tasks/if_task_repository.py
[todo.infrastructure.in_memory.tasks.in_memory_task_repository.py]: ../src/todo/infrastructure/in_memory/tasks/in_memory_task_repository.py

[todo.domain.models.tasks.if_task_factory.py]: ../src/todo/domain/models/tasks/if_task_factory.py
[todo.infrastructure.in_memory.tasks.in_memory_task_factory.py]: ../src/todo/infrastructure/in_memory/tasks/in_memory_task_factory.py
