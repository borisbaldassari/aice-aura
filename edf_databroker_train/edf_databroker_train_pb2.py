# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edf_databroker_train.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='edf_databroker_train.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x65\x64\x66_databroker_train.proto\"\x07\n\x05\x45mpty\"$\n\x07\x45\x64\x66Text\x12\x0b\n\x03\x65\x64\x66\x18\x01 \x01(\t\x12\x0c\n\x04\x61nno\x18\x02 \x01(\t26\n\rEdfDatabroker\x12%\n\x11get_next_edf_file\x12\x06.Empty\x1a\x08.EdfTextb\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
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
  serialized_start=30,
  serialized_end=37,
)


_EDFTEXT = _descriptor.Descriptor(
  name='EdfText',
  full_name='EdfText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='edf', full_name='EdfText.edf', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anno', full_name='EdfText.anno', index=1,
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
  serialized_start=39,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['EdfText'] = _EDFTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'edf_databroker_train_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

EdfText = _reflection.GeneratedProtocolMessageType('EdfText', (_message.Message,), {
  'DESCRIPTOR' : _EDFTEXT,
  '__module__' : 'edf_databroker_train_pb2'
  # @@protoc_insertion_point(class_scope:EdfText)
  })
_sym_db.RegisterMessage(EdfText)



_EDFDATABROKER = _descriptor.ServiceDescriptor(
  name='EdfDatabroker',
  full_name='EdfDatabroker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=77,
  serialized_end=131,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_next_edf_file',
    full_name='EdfDatabroker.get_next_edf_file',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EDFTEXT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EDFDATABROKER)

DESCRIPTOR.services_by_name['EdfDatabroker'] = _EDFDATABROKER

# @@protoc_insertion_point(module_scope)