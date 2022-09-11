"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import todo_pb2 as todo__pb2

class ToDoApplicationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAll = channel.unary_stream('/ToDoApplication/GetAll', request_serializer=todo__pb2.Empty.SerializeToString, response_deserializer=todo__pb2.ToDo.FromString)

class ToDoApplicationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAll(self, request, context):
        """rpc GetById (Empty) returns (ToDo);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ToDoApplicationServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetAll': grpc.unary_stream_rpc_method_handler(servicer.GetAll, request_deserializer=todo__pb2.Empty.FromString, response_serializer=todo__pb2.ToDo.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('ToDoApplication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ToDoApplication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAll(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ToDoApplication/GetAll', todo__pb2.Empty.SerializeToString, todo__pb2.ToDo.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)