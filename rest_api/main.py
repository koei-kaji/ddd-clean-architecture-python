from enum import Enum, unique
from typing import cast

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from rest_api.models.tasks.get.task_get_response import TaskGetResponse
from todo.application.tasks.delete import TaskDeleteInputData, TaskDeleteOutputData
from todo.application.tasks.get_all import TaskGetAllInputData, TaskGetAllOutputData
from todo.application.tasks.get_by_id import TaskGetByIdInputData, TaskGetByIdOutputData
from todo.application.tasks.register import (
    TaskRegisterInputData,
    TaskRegisterOutputData,
)
from todo.application.tasks.update import TaskUpdateInputData, TaskUpdateOutputData
from todo.injector.interactor_bus import InteractorBus

from .models.healthz import HealthzGetResponse
from .models.tasks import (
    TaskDeleteRequest,
    TaskDeleteResponse,
    TaskGetAllResponse,
    TaskPatchRequest,
    TaskPatchResponse,
    TaskPostRequest,
    TaskPostResponse,
)


@unique
class Path(str, Enum):
    healthz = "/healthz"
    todo_all = "/todo"
    todo_by_id = "/todo/{task_id}"


app = FastAPI()

# TODO: config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(Path.healthz.value)
async def healthz() -> HealthzGetResponse:
    return HealthzGetResponse()


@app.get(Path.todo_by_id.value)
async def get_todo_by_id(task_id: str) -> TaskGetResponse:
    input_data = TaskGetByIdInputData(task_id=task_id)
    output_data = cast(TaskGetByIdOutputData, InteractorBus.handle(input_data))
    if output_data.data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return TaskGetResponse(
        id=output_data.data.task_id,
        name=output_data.data.name,
        status=output_data.data.status,
    )


@app.get(Path.todo_all.value)
async def get_todo_all() -> TaskGetAllResponse:
    input_data = TaskGetAllInputData()
    output_data = cast(TaskGetAllOutputData, InteractorBus.handle(input_data))
    data = [
        TaskGetResponse(id=data.task_id, name=data.name, status=data.status)
        for data in output_data.data
    ]
    return TaskGetAllResponse(data=data)


@app.post(Path.todo_all.value, status_code=status.HTTP_201_CREATED)
async def post_todo(request: TaskPostRequest) -> TaskPostResponse:
    input_data = TaskRegisterInputData(name=request.name)
    output_data = cast(TaskRegisterOutputData, InteractorBus.handle(input_data))
    return TaskPostResponse(
        id=output_data.data.task_id,
        name=output_data.data.name,
        status=output_data.data.status,
    )


@app.patch(Path.todo_by_id.value)
async def patch_todo(request: TaskPatchRequest) -> TaskPatchResponse:
    input_data = TaskUpdateInputData(
        task_id=request.id, name=request.name, status=request.status
    )
    _ = cast(TaskUpdateOutputData, InteractorBus.handle(input_data))
    return TaskPatchResponse()


@app.delete(Path.todo_by_id.value)
async def delete_todo(request: TaskDeleteRequest) -> TaskDeleteResponse:
    input_data = TaskDeleteInputData(task_id=request.id)
    _ = cast(TaskDeleteOutputData, InteractorBus.handle(input_data))
    return TaskDeleteResponse()
