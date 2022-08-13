from injector import Binder, Module

from ..application.tasks import IFTaskQueryService
from ..config.task_settings import TaskAdapter, TaskSettings
from ..domain.models.tasks import IFTaskFactory, IFTaskRepository
from ..infrastructure.in_memory.tasks import (
    InMemoryTaskFactory,
    InMemoryTaskQueryService,
    InMemoryTaskRepository,
)
from .exc import AdapterNotFoundError


class TaskModule(Module):
    def configure(self, binder: Binder) -> None:
        settings = TaskSettings()
        match settings.task_adapter:
            case TaskAdapter.in_memory:
                binder.bind(IFTaskFactory, InMemoryTaskFactory)  # type: ignore[misc]
                binder.bind(IFTaskRepository, InMemoryTaskRepository)  # type: ignore[misc]
                binder.bind(IFTaskQueryService, InMemoryTaskQueryService)  # type: ignore[misc]
            case _:
                raise AdapterNotFoundError(
                    f"{settings.task_adapter} adapter was not found."
                )
