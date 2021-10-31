# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aura_dataprep.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="aura_dataprep.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x13\x61ura_dataprep.proto"4\n\x08\x44\x61taFile\x12\x0b\n\x03\x65\x63g\x18\x01 \x01(\t\x12\x0c\n\x04\x61nno\x18\x02 \x01(\t\x12\r\n\x05\x66\x65\x61ts\x18\x03 \x01(\t"$\n\x07\x45\x64\x66\x46ile\x12\x0b\n\x03\x65\x64\x66\x18\x01 \x01(\t\x12\x0c\n\x04\x61nno\x18\x02 \x01(\t25\n\x0c\x41uraDataprep\x12%\n\x0eprepareEdfFile\x12\x08.EdfFile\x1a\t.DataFileb\x06proto3',
)


_DATAFILE = _descriptor.Descriptor(
    name="DataFile",
    full_name="DataFile",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="ecg",
            full_name="DataFile.ecg",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="anno",
            full_name="DataFile.anno",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="feats",
            full_name="DataFile.feats",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=23,
    serialized_end=75,
)


_EDFFILE = _descriptor.Descriptor(
    name="EdfFile",
    full_name="EdfFile",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="edf",
            full_name="EdfFile.edf",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="anno",
            full_name="EdfFile.anno",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=77,
    serialized_end=113,
)

DESCRIPTOR.message_types_by_name["DataFile"] = _DATAFILE
DESCRIPTOR.message_types_by_name["EdfFile"] = _EDFFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataFile = _reflection.GeneratedProtocolMessageType(
    "DataFile",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATAFILE,
        "__module__": "aura_dataprep_pb2"
        # @@protoc_insertion_point(class_scope:DataFile)
    },
)
_sym_db.RegisterMessage(DataFile)

EdfFile = _reflection.GeneratedProtocolMessageType(
    "EdfFile",
    (_message.Message,),
    {
        "DESCRIPTOR": _EDFFILE,
        "__module__": "aura_dataprep_pb2"
        # @@protoc_insertion_point(class_scope:EdfFile)
    },
)
_sym_db.RegisterMessage(EdfFile)


_AURADATAPREP = _descriptor.ServiceDescriptor(
    name="AuraDataprep",
    full_name="AuraDataprep",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=115,
    serialized_end=168,
    methods=[
        _descriptor.MethodDescriptor(
            name="prepareEdfFile",
            full_name="AuraDataprep.prepareEdfFile",
            index=0,
            containing_service=None,
            input_type=_EDFFILE,
            output_type=_DATAFILE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_AURADATAPREP)

DESCRIPTOR.services_by_name["AuraDataprep"] = _AURADATAPREP

# @@protoc_insertion_point(module_scope)