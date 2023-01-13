# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/net/destination.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.net import network_pb2 as common_dot_net_dot_network__pb2
from common.net import address_pb2 as common_dot_net_dot_address__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/net/destination.proto',
  package='xray.common.net',
  syntax='proto3',
  serialized_options=b'\n\023com.xray.common.netP\001Z$github.com/xtls/xray-core/common/net\252\002\017Xray.Common.Net',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x63ommon/net/destination.proto\x12\x0fxray.common.net\x1a\x18\x63ommon/net/network.proto\x1a\x18\x63ommon/net/address.proto\"q\n\x08\x45ndpoint\x12)\n\x07network\x18\x01 \x01(\x0e\x32\x18.xray.common.net.Network\x12,\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x03 \x01(\rBO\n\x13\x63om.xray.common.netP\x01Z$github.com/xtls/xray-core/common/net\xaa\x02\x0fXray.Common.Netb\x06proto3'
  ,
  dependencies=[common_dot_net_dot_network__pb2.DESCRIPTOR,common_dot_net_dot_address__pb2.DESCRIPTOR,])




_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='xray.common.net.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='xray.common.net.Endpoint.network', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='xray.common.net.Endpoint.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='xray.common.net.Endpoint.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=101,
  serialized_end=214,
)

_ENDPOINT.fields_by_name['network'].enum_type = common_dot_net_dot_network__pb2._NETWORK
_ENDPOINT.fields_by_name['address'].message_type = common_dot_net_dot_address__pb2._IPORDOMAIN
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'common.net.destination_pb2'
  # @@protoc_insertion_point(class_scope:xray.common.net.Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
