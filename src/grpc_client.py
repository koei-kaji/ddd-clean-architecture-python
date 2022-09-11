import grpc

from _grpc import todo_pb2, todo_pb2_grpc


def run() -> None:
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoApplicationStub(channel)

        for result in stub.GetAll(todo_pb2.Empty()):
            print(result.id, result.name, result.status)


if __name__ == "__main__":
    print("Get all:")
    run()
