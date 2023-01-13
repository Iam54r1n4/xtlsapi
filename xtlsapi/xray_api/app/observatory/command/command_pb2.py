# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/observatory/command/command.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from app.observatory import config_pb2 as app_dot_observatory_dot_config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/observatory/command/command.proto',
  package='xray.core.app.observatory.command',
  syntax='proto3',
  serialized_options=b'\n%com.xray.core.app.observatory.commandP\001Z1github.com/xtls/xray-core/app/observatory/command\252\002!Xray.Core.App.Observatory.Command',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%app/observatory/command/command.proto\x12!xray.core.app.observatory.command\x1a\x1c\x61pp/observatory/config.proto\"\x1a\n\x18GetOutboundStatusRequest\"Y\n\x19GetOutboundStatusResponse\x12<\n\x06status\x18\x01 \x01(\x0b\x32,.xray.core.app.observatory.ObservationResult\"\x08\n\x06\x43onfig2\xa7\x01\n\x12ObservatoryService\x12\x90\x01\n\x11GetOutboundStatus\x12;.xray.core.app.observatory.command.GetOutboundStatusRequest\x1a<.xray.core.app.observatory.command.GetOutboundStatusResponse\"\x00\x42\x80\x01\n%com.xray.core.app.observatory.commandP\x01Z1github.com/xtls/xray-core/app/observatory/command\xaa\x02!Xray.Core.App.Observatory.Commandb\x06proto3'
  ,
  dependencies=[app_dot_observatory_dot_config__pb2.DESCRIPTOR,])




_GETOUTBOUNDSTATUSREQUEST = _descriptor.Descriptor(
  name='GetOutboundStatusRequest',
  full_name='xray.core.app.observatory.command.GetOutboundStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=132,
)


_GETOUTBOUNDSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetOutboundStatusResponse',
  full_name='xray.core.app.observatory.command.GetOutboundStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='xray.core.app.observatory.command.GetOutboundStatusResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=223,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.core.app.observatory.command.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=233,
)

_GETOUTBOUNDSTATUSRESPONSE.fields_by_name['status'].message_type = app_dot_observatory_dot_config__pb2._OBSERVATIONRESULT
DESCRIPTOR.message_types_by_name['GetOutboundStatusRequest'] = _GETOUTBOUNDSTATUSREQUEST
DESCRIPTOR.message_types_by_name['GetOutboundStatusResponse'] = _GETOUTBOUNDSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetOutboundStatusRequest = _reflection.GeneratedProtocolMessageType('GetOutboundStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOUTBOUNDSTATUSREQUEST,
  '__module__' : 'app.observatory.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.command.GetOutboundStatusRequest)
  })
_sym_db.RegisterMessage(GetOutboundStatusRequest)

GetOutboundStatusResponse = _reflection.GeneratedProtocolMessageType('GetOutboundStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOUTBOUNDSTATUSRESPONSE,
  '__module__' : 'app.observatory.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.command.GetOutboundStatusResponse)
  })
_sym_db.RegisterMessage(GetOutboundStatusResponse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.observatory.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.core.app.observatory.command.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None

_OBSERVATORYSERVICE = _descriptor.ServiceDescriptor(
  name='ObservatoryService',
  full_name='xray.core.app.observatory.command.ObservatoryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=236,
  serialized_end=403,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOutboundStatus',
    full_name='xray.core.app.observatory.command.ObservatoryService.GetOutboundStatus',
    index=0,
    containing_service=None,
    input_type=_GETOUTBOUNDSTATUSREQUEST,
    output_type=_GETOUTBOUNDSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBSERVATORYSERVICE)

DESCRIPTOR.services_by_name['ObservatoryService'] = _OBSERVATORYSERVICE

# @@protoc_insertion_point(module_scope)
