# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello_world.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11hello_world.proto\x12\nhelloworld\"\x1f\n\x0cHelloRequest\x12\x0f\n\x07req_msg\x18\x02 \x01(\t\" \n\rHelloResponse\x12\x0f\n\x07res_msg\x18\x02 \x01(\t2V\n\x11HelloWorldService\x12\x41\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x19.helloworld.HelloResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_world_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=33
  _HELLOREQUEST._serialized_end=64
  _HELLORESPONSE._serialized_start=66
  _HELLORESPONSE._serialized_end=98
  _HELLOWORLDSERVICE._serialized_start=100
  _HELLOWORLDSERVICE._serialized_end=186
# @@protoc_insertion_point(module_scope)