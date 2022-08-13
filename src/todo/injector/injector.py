from injector import Injector

from .task_module import TaskModule

injector = Injector(
    [
        TaskModule,
    ]
)
