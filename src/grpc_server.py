import typing
from concurrent import futures

import grpc

from _grpc import todo_pb2, todo_pb2_grpc
from todo.application.tasks.get_all import TaskGetAllInputData, TaskGetAllOutputData
from todo.injector.interactor_bus import InteractorBus


class ToDoApplicationServicer(todo_pb2_grpc.ToDoApplicationServicer):
    def GetAll(
        self, request: todo_pb2.Empty, context: grpc.ServicerContext
    ) -> typing.Iterator[todo_pb2.ToDo]:
        input_data = TaskGetAllInputData()
        output_data = typing.cast(
            TaskGetAllOutputData, InteractorBus.handle(input_data)
        )
        for data in output_data.data:
            yield todo_pb2.ToDo(id=data.task_id, name=data.name, status=data.status)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    todo_pb2_grpc.add_ToDoApplicationServicer_to_server(
        ToDoApplicationServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running grpc server...")
    serve()
