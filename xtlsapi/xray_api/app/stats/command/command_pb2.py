# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/stats/command/command.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/stats/command/command.proto',
  package='xray.app.stats.command',
  syntax='proto3',
  serialized_options=b'\n\032com.xray.app.stats.commandP\001Z+github.com/xtls/xray-core/app/stats/command\252\002\026Xray.App.Stats.Command',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x61pp/stats/command/command.proto\x12\x16xray.app.stats.command\".\n\x0fGetStatsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05reset\x18\x02 \x01(\x08\"#\n\x04Stat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\">\n\x10GetStatsResponse\x12*\n\x04stat\x18\x01 \x01(\x0b\x32\x1c.xray.app.stats.command.Stat\"3\n\x11QueryStatsRequest\x12\x0f\n\x07pattern\x18\x01 \x01(\t\x12\r\n\x05reset\x18\x02 \x01(\x08\"@\n\x12QueryStatsResponse\x12*\n\x04stat\x18\x01 \x03(\x0b\x32\x1c.xray.app.stats.command.Stat\"\x11\n\x0fSysStatsRequest\"\xc2\x01\n\x10SysStatsResponse\x12\x14\n\x0cNumGoroutine\x18\x01 \x01(\r\x12\r\n\x05NumGC\x18\x02 \x01(\r\x12\r\n\x05\x41lloc\x18\x03 \x01(\x04\x12\x12\n\nTotalAlloc\x18\x04 \x01(\x04\x12\x0b\n\x03Sys\x18\x05 \x01(\x04\x12\x0f\n\x07Mallocs\x18\x06 \x01(\x04\x12\r\n\x05\x46rees\x18\x07 \x01(\x04\x12\x13\n\x0bLiveObjects\x18\x08 \x01(\x04\x12\x14\n\x0cPauseTotalNs\x18\t \x01(\x04\x12\x0e\n\x06Uptime\x18\n \x01(\r\"\x08\n\x06\x43onfig2\xba\x02\n\x0cStatsService\x12_\n\x08GetStats\x12\'.xray.app.stats.command.GetStatsRequest\x1a(.xray.app.stats.command.GetStatsResponse\"\x00\x12\x65\n\nQueryStats\x12).xray.app.stats.command.QueryStatsRequest\x1a*.xray.app.stats.command.QueryStatsResponse\"\x00\x12\x62\n\x0bGetSysStats\x12\'.xray.app.stats.command.SysStatsRequest\x1a(.xray.app.stats.command.SysStatsResponse\"\x00\x42\x64\n\x1a\x63om.xray.app.stats.commandP\x01Z+github.com/xtls/xray-core/app/stats/command\xaa\x02\x16Xray.App.Stats.Commandb\x06proto3'
)




_GETSTATSREQUEST = _descriptor.Descriptor(
  name='GetStatsRequest',
  full_name='xray.app.stats.command.GetStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xray.app.stats.command.GetStatsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reset', full_name='xray.app.stats.command.GetStatsRequest.reset', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=59,
  serialized_end=105,
)


_STAT = _descriptor.Descriptor(
  name='Stat',
  full_name='xray.app.stats.command.Stat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xray.app.stats.command.Stat.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='xray.app.stats.command.Stat.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=107,
  serialized_end=142,
)


_GETSTATSRESPONSE = _descriptor.Descriptor(
  name='GetStatsResponse',
  full_name='xray.app.stats.command.GetStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stat', full_name='xray.app.stats.command.GetStatsResponse.stat', index=0,
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
  serialized_start=144,
  serialized_end=206,
)


_QUERYSTATSREQUEST = _descriptor.Descriptor(
  name='QueryStatsRequest',
  full_name='xray.app.stats.command.QueryStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern', full_name='xray.app.stats.command.QueryStatsRequest.pattern', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reset', full_name='xray.app.stats.command.QueryStatsRequest.reset', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=208,
  serialized_end=259,
)


_QUERYSTATSRESPONSE = _descriptor.Descriptor(
  name='QueryStatsResponse',
  full_name='xray.app.stats.command.QueryStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stat', full_name='xray.app.stats.command.QueryStatsResponse.stat', index=0,
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
  serialized_start=261,
  serialized_end=325,
)


_SYSSTATSREQUEST = _descriptor.Descriptor(
  name='SysStatsRequest',
  full_name='xray.app.stats.command.SysStatsRequest',
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
  serialized_start=327,
  serialized_end=344,
)


_SYSSTATSRESPONSE = _descriptor.Descriptor(
  name='SysStatsResponse',
  full_name='xray.app.stats.command.SysStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='NumGoroutine', full_name='xray.app.stats.command.SysStatsResponse.NumGoroutine', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='NumGC', full_name='xray.app.stats.command.SysStatsResponse.NumGC', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Alloc', full_name='xray.app.stats.command.SysStatsResponse.Alloc', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TotalAlloc', full_name='xray.app.stats.command.SysStatsResponse.TotalAlloc', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Sys', full_name='xray.app.stats.command.SysStatsResponse.Sys', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Mallocs', full_name='xray.app.stats.command.SysStatsResponse.Mallocs', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Frees', full_name='xray.app.stats.command.SysStatsResponse.Frees', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LiveObjects', full_name='xray.app.stats.command.SysStatsResponse.LiveObjects', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PauseTotalNs', full_name='xray.app.stats.command.SysStatsResponse.PauseTotalNs', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Uptime', full_name='xray.app.stats.command.SysStatsResponse.Uptime', index=9,
      number=10, type=13, cpp_type=3, label=1,
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
  serialized_start=347,
  serialized_end=541,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='xray.app.stats.command.Config',
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
  serialized_start=543,
  serialized_end=551,
)

_GETSTATSRESPONSE.fields_by_name['stat'].message_type = _STAT
_QUERYSTATSRESPONSE.fields_by_name['stat'].message_type = _STAT
DESCRIPTOR.message_types_by_name['GetStatsRequest'] = _GETSTATSREQUEST
DESCRIPTOR.message_types_by_name['Stat'] = _STAT
DESCRIPTOR.message_types_by_name['GetStatsResponse'] = _GETSTATSRESPONSE
DESCRIPTOR.message_types_by_name['QueryStatsRequest'] = _QUERYSTATSREQUEST
DESCRIPTOR.message_types_by_name['QueryStatsResponse'] = _QUERYSTATSRESPONSE
DESCRIPTOR.message_types_by_name['SysStatsRequest'] = _SYSSTATSREQUEST
DESCRIPTOR.message_types_by_name['SysStatsResponse'] = _SYSSTATSRESPONSE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStatsRequest = _reflection.GeneratedProtocolMessageType('GetStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATSREQUEST,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.GetStatsRequest)
  })
_sym_db.RegisterMessage(GetStatsRequest)

Stat = _reflection.GeneratedProtocolMessageType('Stat', (_message.Message,), {
  'DESCRIPTOR' : _STAT,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.Stat)
  })
_sym_db.RegisterMessage(Stat)

GetStatsResponse = _reflection.GeneratedProtocolMessageType('GetStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATSRESPONSE,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.GetStatsResponse)
  })
_sym_db.RegisterMessage(GetStatsResponse)

QueryStatsRequest = _reflection.GeneratedProtocolMessageType('QueryStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSTATSREQUEST,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.QueryStatsRequest)
  })
_sym_db.RegisterMessage(QueryStatsRequest)

QueryStatsResponse = _reflection.GeneratedProtocolMessageType('QueryStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSTATSRESPONSE,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.QueryStatsResponse)
  })
_sym_db.RegisterMessage(QueryStatsResponse)

SysStatsRequest = _reflection.GeneratedProtocolMessageType('SysStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYSSTATSREQUEST,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.SysStatsRequest)
  })
_sym_db.RegisterMessage(SysStatsRequest)

SysStatsResponse = _reflection.GeneratedProtocolMessageType('SysStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYSSTATSRESPONSE,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.SysStatsResponse)
  })
_sym_db.RegisterMessage(SysStatsResponse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.stats.command.command_pb2'
  # @@protoc_insertion_point(class_scope:xray.app.stats.command.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None

_STATSSERVICE = _descriptor.ServiceDescriptor(
  name='StatsService',
  full_name='xray.app.stats.command.StatsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=554,
  serialized_end=868,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStats',
    full_name='xray.app.stats.command.StatsService.GetStats',
    index=0,
    containing_service=None,
    input_type=_GETSTATSREQUEST,
    output_type=_GETSTATSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryStats',
    full_name='xray.app.stats.command.StatsService.QueryStats',
    index=1,
    containing_service=None,
    input_type=_QUERYSTATSREQUEST,
    output_type=_QUERYSTATSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSysStats',
    full_name='xray.app.stats.command.StatsService.GetSysStats',
    index=2,
    containing_service=None,
    input_type=_SYSSTATSREQUEST,
    output_type=_SYSSTATSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATSSERVICE)

DESCRIPTOR.services_by_name['StatsService'] = _STATSSERVICE

# @@protoc_insertion_point(module_scope)
