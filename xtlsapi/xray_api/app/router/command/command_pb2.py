# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/router/command/command.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.net import network_pb2 as common_dot_net_dot_network__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/router/command/command.proto',
  package='xray.app.router.command',
  syntax='proto3',
  serialized_options=b'\n\033com.xray.app.router.commandP\001Z,github.com/xtls/xray-core/app/router/command\252\002\027Xray.App.Router.Command',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n app/router/command/command.proto\x12\x17xray.app.router.command\x1a\x18\x63ommon/net/network.proto\"\x83\x03\n\x0eRoutingContext\x12\x12\n\nInboundTag\x18\x01 \x01(\t\x12)\n\x07Network\x18\x02 \x01(\x0e\x32\x18.xray.common.net.Network\x12\x11\n\tSourceIPs\x18\x03 \x03(\x0c\x12\x11\n\tTargetIPs\x18\x04 \x03(\x0c\x12\x12\n\nSourcePort\x18\x05 \x01(\r\x12\x12\n\nTargetPort\x18\x06 \x01(\r\x12\x14\n\x0cTargetDomain\x18\x07 \x01(\t\x12\x10\n\x08Protocol\x18\x08 \x01(\t\x12\x0c\n\x04User\x18\t \x01(\t\x12K\n\nAttributes\x18\n \x03(\x0b\x32\x37.xray.app.router.command.RoutingContext.AttributesEntry\x12\x19\n\x11OutboundGroupTags\x18\x0b \x03(\t\x12\x13\n\x0bOutboundTag\x18\x0c \x01(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"6\n\x1cSubscribeRoutingStatsRequest\x12\x16\n\x0e\x46ieldSelectors\x18\x01 \x03(\t\"\x82\x01\n\x10TestRouteRequest\x12?\n\x0eRoutingContext\x18\x01 \x01(\x0b\x32\'.xray.app.router.command.RoutingContext\x12\x16\n\x0e\x46ieldSelectors\x18\x02 \x03(\t\x12\x15\n\rPublishResult\x18\x03 \x01(\x08\"\x08\n\x06\x43onfig2\xf0\x01\n\x0eRoutingService\x12{\n\x15SubscribeRoutingStats\x12\x35.xray.app.router.command.SubscribeRoutingStatsRequest\x1a\'.xray.app.router.command.RoutingContext\"\x00\x30\x01\x12\x61\n\tTestRoute\x12).xray.app.router.command.TestRouteRequest\x1a\'.xray.app.router.command.RoutingContext\"\x00\x42g\n\x1b\x63om.xray.app.router.commandP\x01Z,github.com/xtls/xray-core/app/router/command\xaa\x02\x17Xray.App.Router.Commandb\x06proto3'
  ,
  dependencies=[common_dot_net_dot_network__pb2.DESCRIPTOR,])




_ROUTINGCONTEXT_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='xray.app.router.command.RoutingContext.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='xray.app.router.command.RoutingContext.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='xray.app.router.command.RoutingContext.AttributesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=475,
)

_ROUTINGCONTEXT = _descriptor.Descriptor(
  name='RoutingContext',
  full_name='xray.app.router.command.RoutingContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='InboundTag', full_name='xray.app.router.command.RoutingContext.InboundTag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Network', full_name='xray.app.router.command.RoutingContext.Network', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SourceIPs', full_name='xray.app.router.command.RoutingContext.SourceIPs', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TargetIPs', full_name='xray.app.router.command.RoutingContext.TargetIPs', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SourcePort', full_name='xray.app.router.command.RoutingContext.SourcePort', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TargetPort', full_name='xray.app.router.command.RoutingContext.TargetPort', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TargetDomain', full_name='xray.app.router.command.RoutingContext.TargetDomain', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Protocol', full_name='xray.app.router.command.RoutingContext.Protocol', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='User', full_name='xray.app.router.command.RoutingContext.User', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Attributes', full_name='xray.app.router.command.RoutingContext.Attributes', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OutboundGroupTags', full_name='xray.app.router.command.RoutingContext.OutboundGroupTags', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OutboundTag', full_name='xray.app.router.command.RoutingContext.OutboundTag', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ROUTINGCONTEXT_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=475,
)


_SUBSCRIBEROUTINGSTATSREQUEST = _descriptor.Descriptor(
  name='SubscribeRoutingStatsRequest',
  full_name='xray.app.router.command.SubscribeRoutingStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='FieldSelectors', full_name='xray.app.router.command.SubscribeRoutingStatsRequest.FieldSelectors', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=477,
  serialized_end=531,
)


_TESTROUTEREQUEST = _descriptor.Descriptor(
  name='TestRouteRequest',
  full_name='xray.app.router.command.TestRouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='RoutingContext', full_name='xray.app.router.command.TestRouteRequest.RoutingContext', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FieldSelectors', full_name='xray.app.router.command.TestRouteRequest.FieldSelectors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PublishResult', full_name='xray.app.router.command.TestRouteRequest.PublishResult', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=534,
  serialized_end=664,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.app.router.command.Config',
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
  serialized_start=666,
  serialized_end=674,
)

_ROUTINGCONTEXT_ATTRIBUTESENTRY.containing_type = _ROUTINGCONTEXT
_ROUTINGCONTEXT.fields_by_name['Network'].enum_type = common_dot_net_dot_network__pb2._NETWORK
_ROUTINGCONTEXT.fields_by_name['Attributes'].message_type = _ROUTINGCONTEXT_ATTRIBUTESENTRY
_TESTROUTEREQUEST.fields_by_name['RoutingContext'].message_type = _ROUTINGCONTEXT
DESCRIPTOR.message_types_by_name['RoutingContext'] = _ROUTINGCONTEXT
DESCRIPTOR.message_types_by_name['SubscribeRoutingStatsRequest'] = _SUBSCRIBEROUTINGSTATSREQUEST
DESCRIPTOR.message_types_by_name['TestRouteRequest'] = _TESTROUTEREQUEST
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoutingContext = _reflection.GeneratedProtocolMessageType('RoutingContext', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _ROUTINGCONTEXT_ATTRIBUTESENTRY,
    '__module__' : 'app.router.command.command_pb2'
    # @@protoc_insertion_point(class_scope:xray.app.router.command.RoutingContext.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _ROUTINGCONTEXT,
  '__module__' : 'app.router.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.command.RoutingContext)
  })
_sym_db.RegisterMessage(RoutingContext)
_sym_db.RegisterMessage(RoutingContext.AttributesEntry)

SubscribeRoutingStatsRequest = _reflection.GeneratedProtocolMessageType('SubscribeRoutingStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEROUTINGSTATSREQUEST,
  '__module__' : 'app.router.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.command.SubscribeRoutingStatsRequest)
  })
_sym_db.RegisterMessage(SubscribeRoutingStatsRequest)

TestRouteRequest = _reflection.GeneratedProtocolMessageType('TestRouteRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTROUTEREQUEST,
  '__module__' : 'app.router.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.command.TestRouteRequest)
  })
_sym_db.RegisterMessage(TestRouteRequest)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.router.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.router.command.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
_ROUTINGCONTEXT_ATTRIBUTESENTRY._options = None

_ROUTINGSERVICE = _descriptor.ServiceDescriptor(
  name='RoutingService',
  full_name='xray.app.router.command.RoutingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=677,
  serialized_end=917,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeRoutingStats',
    full_name='xray.app.router.command.RoutingService.SubscribeRoutingStats',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBEROUTINGSTATSREQUEST,
    output_type=_ROUTINGCONTEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestRoute',
    full_name='xray.app.router.command.RoutingService.TestRoute',
    index=1,
    containing_service=None,
    input_type=_TESTROUTEREQUEST,
    output_type=_ROUTINGCONTEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTINGSERVICE)

DESCRIPTOR.services_by_name['RoutingService'] = _ROUTINGSERVICE

# @@protoc_insertion_point(module_scope)
