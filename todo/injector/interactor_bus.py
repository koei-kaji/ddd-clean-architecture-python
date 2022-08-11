from ..application.abc import ABCInputData, ABCOutputData
from ..application.tasks.delete import TaskDeleteInputData, TaskDeleteInteractor
from ..application.tasks.get_all import TaskGetAllInputData, TaskGetAllInteractor
from ..application.tasks.get_by_id import TaskGetByIdInputData, TaskGetByIdInteractor
from ..application.tasks.register import TaskRegisterInputData, TaskRegisterInteractor
from ..application.tasks.update import TaskUpdateInputData, TaskUpdateInteractor
from .exc import InteractorNotFoundError
from .injector import injector


class InteractorBus:
    @staticmethod
    def handle(input_data: ABCInputData) -> ABCOutputData:
        match input_data.__class__.__name__:
            case TaskDeleteInputData.__name__:
                return injector.get(TaskDeleteInteractor).handle(input_data)
            case TaskGetByIdInputData.__name__:
                return injector.get(TaskGetByIdInteractor).handle(input_data)
            case TaskGetAllInputData.__name__:
                return injector.get(TaskGetAllInteractor).handle(input_data)
            case TaskRegisterInputData.__name__:
                return injector.get(TaskRegisterInteractor).handle(input_data)
            case TaskUpdateInputData.__name__:
                return injector.get(TaskUpdateInteractor).handle(input_data)
            case _:
                raise InteractorNotFoundError(
                    f"Interactor corresponding to {input_data.__class__.__name__} was not found."
                )
