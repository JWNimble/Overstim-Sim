# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/audio_to_tensor_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/tensor/audio_to_tensor_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n=mediapipe/calculators/tensor/audio_to_tensor_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa9\x06\n\x1e\x41udioToTensorCalculatorOptions\x12\x14\n\x0cnum_channels\x18\x01 \x01(\x03\x12\x13\n\x0bnum_samples\x18\x02 \x01(\x03\x12\"\n\x17num_overlapping_samples\x18\x03 \x01(\x03:\x01\x30\x12\x1a\n\x12target_sample_rate\x18\x04 \x01(\x01\x12\x19\n\x0bstream_mode\x18\x05 \x01(\x08:\x04true\x12+\n\x1d\x63heck_inconsistent_timestamps\x18\x06 \x01(\x08:\x04true\x12\x10\n\x08\x66\x66t_size\x18\x07 \x01(\x03\x12\x1e\n\x16padding_samples_before\x18\x08 \x01(\x03\x12\x1d\n\x15padding_samples_after\x18\t \x01(\x03\x12\x65\n\nflush_mode\x18\n \x01(\x0e\x32\x33.mediapipe.AudioToTensorCalculatorOptions.FlushMode:\x1c\x45NTIRE_TAIL_AT_TIMESTAMP_MAX\x12\x62\n\x11\x64\x66t_tensor_format\x18\x0b \x01(\x0e\x32\x39.mediapipe.AudioToTensorCalculatorOptions.DftTensorFormat:\x0cWITH_NYQUIST\x12\x16\n\x0evolume_gain_db\x18\x0c \x01(\x01\"M\n\tFlushMode\x12\x08\n\x04NONE\x10\x00\x12 \n\x1c\x45NTIRE_TAIL_AT_TIMESTAMP_MAX\x10\x01\x12\x14\n\x10PROCEED_AS_USUAL\x10\x02\"w\n\x0f\x44\x66tTensorFormat\x12\x1d\n\x19\x44\x46T_TENSOR_FORMAT_UNKNOWN\x10\x00\x12\x1a\n\x16WITHOUT_DC_AND_NYQUIST\x10\x01\x12\x10\n\x0cWITH_NYQUIST\x10\x02\x12\x17\n\x13WITH_DC_AND_NYQUIST\x10\x03\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb8\xc1\xf6\xd5\x01 \x01(\x0b\x32).mediapipe.AudioToTensorCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE = _descriptor.EnumDescriptor(
  name='FlushMode',
  full_name='mediapipe.AudioToTensorCalculatorOptions.FlushMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTIRE_TAIL_AT_TIMESTAMP_MAX', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCEED_AS_USUAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=636,
  serialized_end=713,
)
_sym_db.RegisterEnumDescriptor(_AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE)

_AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT = _descriptor.EnumDescriptor(
  name='DftTensorFormat',
  full_name='mediapipe.AudioToTensorCalculatorOptions.DftTensorFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DFT_TENSOR_FORMAT_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITHOUT_DC_AND_NYQUIST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITH_NYQUIST', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITH_DC_AND_NYQUIST', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=715,
  serialized_end=834,
)
_sym_db.RegisterEnumDescriptor(_AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT)


_AUDIOTOTENSORCALCULATOROPTIONS = _descriptor.Descriptor(
  name='AudioToTensorCalculatorOptions',
  full_name='mediapipe.AudioToTensorCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_channels', full_name='mediapipe.AudioToTensorCalculatorOptions.num_channels', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_samples', full_name='mediapipe.AudioToTensorCalculatorOptions.num_samples', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_overlapping_samples', full_name='mediapipe.AudioToTensorCalculatorOptions.num_overlapping_samples', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_sample_rate', full_name='mediapipe.AudioToTensorCalculatorOptions.target_sample_rate', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_mode', full_name='mediapipe.AudioToTensorCalculatorOptions.stream_mode', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_inconsistent_timestamps', full_name='mediapipe.AudioToTensorCalculatorOptions.check_inconsistent_timestamps', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fft_size', full_name='mediapipe.AudioToTensorCalculatorOptions.fft_size', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='padding_samples_before', full_name='mediapipe.AudioToTensorCalculatorOptions.padding_samples_before', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='padding_samples_after', full_name='mediapipe.AudioToTensorCalculatorOptions.padding_samples_after', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flush_mode', full_name='mediapipe.AudioToTensorCalculatorOptions.flush_mode', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dft_tensor_format', full_name='mediapipe.AudioToTensorCalculatorOptions.dft_tensor_format', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume_gain_db', full_name='mediapipe.AudioToTensorCalculatorOptions.volume_gain_db', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.AudioToTensorCalculatorOptions.ext', index=0,
      number=448635064, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE,
    _AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=924,
)

_AUDIOTOTENSORCALCULATOROPTIONS.fields_by_name['flush_mode'].enum_type = _AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE
_AUDIOTOTENSORCALCULATOROPTIONS.fields_by_name['dft_tensor_format'].enum_type = _AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT
_AUDIOTOTENSORCALCULATOROPTIONS_FLUSHMODE.containing_type = _AUDIOTOTENSORCALCULATOROPTIONS
_AUDIOTOTENSORCALCULATOROPTIONS_DFTTENSORFORMAT.containing_type = _AUDIOTOTENSORCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['AudioToTensorCalculatorOptions'] = _AUDIOTOTENSORCALCULATOROPTIONS

AudioToTensorCalculatorOptions = _reflection.GeneratedProtocolMessageType('AudioToTensorCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOTOTENSORCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.audio_to_tensor_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.AudioToTensorCalculatorOptions)
  ))
_sym_db.RegisterMessage(AudioToTensorCalculatorOptions)

_AUDIOTOTENSORCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _AUDIOTOTENSORCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_AUDIOTOTENSORCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
