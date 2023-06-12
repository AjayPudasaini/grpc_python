from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ["req_msg"]
    REQ_MSG_FIELD_NUMBER: _ClassVar[int]
    req_msg: str
    def __init__(self, req_msg: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ["res_msg"]
    RES_MSG_FIELD_NUMBER: _ClassVar[int]
    res_msg: str
    def __init__(self, res_msg: _Optional[str] = ...) -> None: ...
