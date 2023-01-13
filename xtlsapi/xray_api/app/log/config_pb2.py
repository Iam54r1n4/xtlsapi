# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/log/config.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.log import log_pb2 as common_dot_log_dot_log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/log/config.proto',
  package='xray.app.log',
  syntax='proto3',
  serialized_options=b'\n\020com.xray.app.logP\001Z!github.com/xtls/xray-core/app/log\252\002\014Xray.App.Log',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x61pp/log/config.proto\x12\x0cxray.app.log\x1a\x14\x63ommon/log/log.proto\"\xe4\x01\n\x06\x43onfig\x12-\n\x0e\x65rror_log_type\x18\x01 \x01(\x0e\x32\x15.xray.app.log.LogType\x12\x32\n\x0f\x65rror_log_level\x18\x02 \x01(\x0e\x32\x19.xray.common.log.Severity\x12\x16\n\x0e\x65rror_log_path\x18\x03 \x01(\t\x12.\n\x0f\x61\x63\x63\x65ss_log_type\x18\x04 \x01(\x0e\x32\x15.xray.app.log.LogType\x12\x17\n\x0f\x61\x63\x63\x65ss_log_path\x18\x05 \x01(\t\x12\x16\n\x0e\x65nable_dns_log\x18\x06 \x01(\x08*5\n\x07LogType\x12\x08\n\x04None\x10\x00\x12\x0b\n\x07\x43onsole\x10\x01\x12\x08\n\x04\x46ile\x10\x02\x12\t\n\x05\x45vent\x10\x03\x42\x46\n\x10\x63om.xray.app.logP\x01Z!github.com/xtls/xray-core/app/log\xaa\x02\x0cXray.App.Logb\x06proto3'
  ,
  dependencies=[common_dot_log_dot_log__pb2.DESCRIPTOR,])

_LOGTYPE = _descriptor.EnumDescriptor(
  name='LogType',
  full_name='xray.app.log.LogType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='None', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Console', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='File', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Event', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=291,
  serialized_end=344,
)
_sym_db.RegisterEnumDescriptor(_LOGTYPE)

LogType = enum_type_wrapper.EnumTypeWrapper(_LOGTYPE)
globals()['None'] = 0
Console = 1
File = 2
Event = 3



_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.app.log.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_log_type', full_name='xray.app.log.Config.error_log_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_log_level', full_name='xray.app.log.Config.error_log_level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_log_path', full_name='xray.app.log.Config.error_log_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_log_type', full_name='xray.app.log.Config.access_log_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_log_path', full_name='xray.app.log.Config.access_log_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_dns_log', full_name='xray.app.log.Config.enable_dns_log', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=61,
  serialized_end=289,
)

_CONFIG.fields_by_name['error_log_type'].enum_type = _LOGTYPE
_CONFIG.fields_by_name['error_log_level'].enum_type = common_dot_log_dot_log__pb2._SEVERITY
_CONFIG.fields_by_name['access_log_type'].enum_type = _LOGTYPE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.enum_types_by_name['LogType'] = _LOGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.log.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.log.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
