from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuildPromptRequest(_message.Message):
    __slots__ = ("req_id", "client_id", "prompt_id", "records_source_id", "prompt_templates_source_id", "from_time", "to_time")
    REQ_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDS_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEMPLATES_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_TIME_FIELD_NUMBER: _ClassVar[int]
    TO_TIME_FIELD_NUMBER: _ClassVar[int]
    req_id: str
    client_id: str
    prompt_id: int
    records_source_id: str
    prompt_templates_source_id: str
    from_time: str
    to_time: str
    def __init__(self, req_id: _Optional[str] = ..., client_id: _Optional[str] = ..., prompt_id: _Optional[int] = ..., records_source_id: _Optional[str] = ..., prompt_templates_source_id: _Optional[str] = ..., from_time: _Optional[str] = ..., to_time: _Optional[str] = ...) -> None: ...

class BuildPromptResponse(_message.Message):
    __slots__ = ("prompt",)
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    def __init__(self, prompt: _Optional[str] = ...) -> None: ...
