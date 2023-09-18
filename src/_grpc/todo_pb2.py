"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto"\x07\n\x05Empty"0\n\x04ToDo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t2,\n\x0fToDoApplication\x12\x19\n\x06GetAll\x12\x06.Empty\x1a\x05.ToDo0\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_EMPTY']._serialized_start = 14
    _globals['_EMPTY']._serialized_end = 21
    _globals['_TODO']._serialized_start = 23
    _globals['_TODO']._serialized_end = 71
    _globals['_TODOAPPLICATION']._serialized_start = 73
    _globals['_TODOAPPLICATION']._serialized_end = 117