# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/headers/http/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transport/internet/headers/http/config.proto',
  package='xray.transport.internet.headers.http',
  syntax='proto3',
  serialized_options=b'\n(com.xray.transport.internet.headers.httpP\001Z9github.com/xtls/xray-core/transport/internet/headers/http\252\002$Xray.Transport.Internet.Headers.Http',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,transport/internet/headers/http/config.proto\x12$xray.transport.internet.headers.http\"%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x03(\t\"\x18\n\x07Version\x12\r\n\x05value\x18\x01 \x01(\t\"\x17\n\x06Method\x12\r\n\x05value\x18\x01 \x01(\t\"\xd8\x01\n\rRequestConfig\x12>\n\x07version\x18\x01 \x01(\x0b\x32-.xray.transport.internet.headers.http.Version\x12<\n\x06method\x18\x02 \x01(\x0b\x32,.xray.transport.internet.headers.http.Method\x12\x0b\n\x03uri\x18\x03 \x03(\t\x12<\n\x06header\x18\x04 \x03(\x0b\x32,.xray.transport.internet.headers.http.Header\"&\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\xcc\x01\n\x0eResponseConfig\x12>\n\x07version\x18\x01 \x01(\x0b\x32-.xray.transport.internet.headers.http.Version\x12<\n\x06status\x18\x02 \x01(\x0b\x32,.xray.transport.internet.headers.http.Status\x12<\n\x06header\x18\x03 \x03(\x0b\x32,.xray.transport.internet.headers.http.Header\"\x96\x01\n\x06\x43onfig\x12\x44\n\x07request\x18\x01 \x01(\x0b\x32\x33.xray.transport.internet.headers.http.RequestConfig\x12\x46\n\x08response\x18\x02 \x01(\x0b\x32\x34.xray.transport.internet.headers.http.ResponseConfigB\x8e\x01\n(com.xray.transport.internet.headers.httpP\x01Z9github.com/xtls/xray-core/transport/internet/headers/http\xaa\x02$Xray.Transport.Internet.Headers.Httpb\x06proto3'
)




_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='xray.transport.internet.headers.http.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xray.transport.internet.headers.http.Header.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='xray.transport.internet.headers.http.Header.value', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=86,
  serialized_end=123,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='xray.transport.internet.headers.http.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xray.transport.internet.headers.http.Version.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=125,
  serialized_end=149,
)


_METHOD = _descriptor.Descriptor(
  name='Method',
  full_name='xray.transport.internet.headers.http.Method',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xray.transport.internet.headers.http.Method.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=151,
  serialized_end=174,
)


_REQUESTCONFIG = _descriptor.Descriptor(
  name='RequestConfig',
  full_name='xray.transport.internet.headers.http.RequestConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='xray.transport.internet.headers.http.RequestConfig.version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method', full_name='xray.transport.internet.headers.http.RequestConfig.method', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='xray.transport.internet.headers.http.RequestConfig.uri', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='xray.transport.internet.headers.http.RequestConfig.header', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=177,
  serialized_end=393,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='xray.transport.internet.headers.http.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='xray.transport.internet.headers.http.Status.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='xray.transport.internet.headers.http.Status.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=395,
  serialized_end=433,
)


_RESPONSECONFIG = _descriptor.Descriptor(
  name='ResponseConfig',
  full_name='xray.transport.internet.headers.http.ResponseConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='xray.transport.internet.headers.http.ResponseConfig.version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='xray.transport.internet.headers.http.ResponseConfig.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='xray.transport.internet.headers.http.ResponseConfig.header', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=436,
  serialized_end=640,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.transport.internet.headers.http.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='xray.transport.internet.headers.http.Config.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='xray.transport.internet.headers.http.Config.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=643,
  serialized_end=793,
)

_REQUESTCONFIG.fields_by_name['version'].message_type = _VERSION
_REQUESTCONFIG.fields_by_name['method'].message_type = _METHOD
_REQUESTCONFIG.fields_by_name['header'].message_type = _HEADER
_RESPONSECONFIG.fields_by_name['version'].message_type = _VERSION
_RESPONSECONFIG.fields_by_name['status'].message_type = _STATUS
_RESPONSECONFIG.fields_by_name['header'].message_type = _HEADER
_CONFIG.fields_by_name['request'].message_type = _REQUESTCONFIG
_CONFIG.fields_by_name['response'].message_type = _RESPONSECONFIG
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['Method'] = _METHOD
DESCRIPTOR.message_types_by_name['RequestConfig'] = _REQUESTCONFIG
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['ResponseConfig'] = _RESPONSECONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Header)
  })
_sym_db.RegisterMessage(Header)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Version)
  })
_sym_db.RegisterMessage(Version)

Method = _reflection.GeneratedProtocolMessageType('Method', (_message.Message,), {
  'DESCRIPTOR' : _METHOD,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Method)
  })
_sym_db.RegisterMessage(Method)

RequestConfig = _reflection.GeneratedProtocolMessageType('RequestConfig', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCONFIG,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.RequestConfig)
  })
_sym_db.RegisterMessage(RequestConfig)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Status)
  })
_sym_db.RegisterMessage(Status)

ResponseConfig = _reflection.GeneratedProtocolMessageType('ResponseConfig', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECONFIG,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.ResponseConfig)
  })
_sym_db.RegisterMessage(ResponseConfig)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.internet.headers.http.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.http.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
