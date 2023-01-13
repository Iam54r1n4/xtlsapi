# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/trojan/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.protocol import user_pb2 as common_dot_protocol_dot_user__pb2
from common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/trojan/config.proto',
  package='xray.proxy.trojan',
  syntax='proto3',
  serialized_options=b'\n\025com.xray.proxy.trojanP\001Z&github.com/xtls/xray-core/proxy/trojan\252\002\021Xray.Proxy.Trojan',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19proxy/trojan/config.proto\x12\x11xray.proxy.trojan\x1a\x1a\x63ommon/protocol/user.proto\x1a!common/protocol/server_spec.proto\")\n\x07\x41\x63\x63ount\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x0c\n\x04\x66low\x18\x02 \x01(\t\"^\n\x08\x46\x61llback\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x61lpn\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x05 \x01(\t\x12\x0c\n\x04xver\x18\x06 \x01(\x04\"D\n\x0c\x43lientConfig\x12\x34\n\x06server\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpoint\"i\n\x0cServerConfig\x12)\n\x05users\x18\x01 \x03(\x0b\x32\x1a.xray.common.protocol.User\x12.\n\tfallbacks\x18\x03 \x03(\x0b\x32\x1b.xray.proxy.trojan.FallbackBU\n\x15\x63om.xray.proxy.trojanP\x01Z&github.com/xtls/xray-core/proxy/trojan\xaa\x02\x11Xray.Proxy.Trojanb\x06proto3'
  ,
  dependencies=[common_dot_protocol_dot_user__pb2.DESCRIPTOR,common_dot_protocol_dot_server__spec__pb2.DESCRIPTOR,])




_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='xray.proxy.trojan.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='password', full_name='xray.proxy.trojan.Account.password', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow', full_name='xray.proxy.trojan.Account.flow', index=1,
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
  serialized_start=111,
  serialized_end=152,
)


_FALLBACK = _descriptor.Descriptor(
  name='Fallback',
  full_name='xray.proxy.trojan.Fallback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xray.proxy.trojan.Fallback.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alpn', full_name='xray.proxy.trojan.Fallback.alpn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='xray.proxy.trojan.Fallback.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='xray.proxy.trojan.Fallback.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dest', full_name='xray.proxy.trojan.Fallback.dest', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='xver', full_name='xray.proxy.trojan.Fallback.xver', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=154,
  serialized_end=248,
)


_CLIENTCONFIG = _descriptor.Descriptor(
  name='ClientConfig',
  full_name='xray.proxy.trojan.ClientConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='xray.proxy.trojan.ClientConfig.server', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=250,
  serialized_end=318,
)


_SERVERCONFIG = _descriptor.Descriptor(
  name='ServerConfig',
  full_name='xray.proxy.trojan.ServerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='xray.proxy.trojan.ServerConfig.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fallbacks', full_name='xray.proxy.trojan.ServerConfig.fallbacks', index=1,
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
  serialized_start=320,
  serialized_end=425,
)

_CLIENTCONFIG.fields_by_name['server'].message_type = common_dot_protocol_dot_server__spec__pb2._SERVERENDPOINT
_SERVERCONFIG.fields_by_name['users'].message_type = common_dot_protocol_dot_user__pb2._USER
_SERVERCONFIG.fields_by_name['fallbacks'].message_type = _FALLBACK
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Fallback'] = _FALLBACK
DESCRIPTOR.message_types_by_name['ClientConfig'] = _CLIENTCONFIG
DESCRIPTOR.message_types_by_name['ServerConfig'] = _SERVERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.trojan.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.trojan.Account)
  })
_sym_db.RegisterMessage(Account)

Fallback = _reflection.GeneratedProtocolMessageType('Fallback', (_message.Message,), {
  'DESCRIPTOR' : _FALLBACK,
  '__module__' : 'proxy.trojan.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.trojan.Fallback)
  })
_sym_db.RegisterMessage(Fallback)

ClientConfig = _reflection.GeneratedProtocolMessageType('ClientConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTCONFIG,
  '__module__' : 'proxy.trojan.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.trojan.ClientConfig)
  })
_sym_db.RegisterMessage(ClientConfig)

ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVERCONFIG,
  '__module__' : 'proxy.trojan.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.trojan.ServerConfig)
  })
_sym_db.RegisterMessage(ServerConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
