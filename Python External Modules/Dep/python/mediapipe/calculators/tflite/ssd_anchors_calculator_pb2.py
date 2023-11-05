# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tflite/ssd_anchors_calculator.proto

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
from mediapipe.framework.formats.object_detection import anchor_pb2 as mediapipe_dot_framework_dot_formats_dot_object__detection_dot_anchor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/tflite/ssd_anchors_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n9mediapipe/calculators/tflite/ssd_anchors_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x39mediapipe/framework/formats/object_detection/anchor.proto\"\xd7\x05\n\x1bSsdAnchorsCalculatorOptions\x12\x18\n\x10input_size_width\x18\x01 \x01(\x05\x12\x19\n\x11input_size_height\x18\x02 \x01(\x05\x12\x11\n\tmin_scale\x18\x03 \x01(\x02\x12\x11\n\tmax_scale\x18\x04 \x01(\x02\x12\x1c\n\x0f\x61nchor_offset_x\x18\x05 \x01(\x02:\x03\x30.5\x12\x1c\n\x0f\x61nchor_offset_y\x18\x06 \x01(\x02:\x03\x30.5\x12\x12\n\nnum_layers\x18\x07 \x01(\x05\x12\x19\n\x11\x66\x65\x61ture_map_width\x18\x08 \x03(\x05\x12\x1a\n\x12\x66\x65\x61ture_map_height\x18\t \x03(\x05\x12\x0f\n\x07strides\x18\n \x03(\x05\x12\x15\n\raspect_ratios\x18\x0b \x03(\x02\x12+\n\x1creduce_boxes_in_lowest_layer\x18\x0c \x01(\x08:\x05\x66\x61lse\x12*\n\x1finterpolated_scale_aspect_ratio\x18\r \x01(\x02:\x01\x31\x12 \n\x11\x66ixed_anchor_size\x18\x0e \x01(\x08:\x05\x66\x61lse\x12+\n\x1cmultiscale_anchor_generation\x18\x0f \x01(\x08:\x05\x66\x61lse\x12\x14\n\tmin_level\x18\x10 \x01(\x05:\x01\x33\x12\x14\n\tmax_level\x18\x11 \x01(\x05:\x01\x37\x12\x17\n\x0c\x61nchor_scale\x18\x12 \x01(\x02:\x01\x34\x12\x1c\n\x11scales_per_octave\x18\x13 \x01(\x05:\x01\x32\x12#\n\x15normalize_coordinates\x18\x14 \x01(\x08:\x04true\x12(\n\rfixed_anchors\x18\x15 \x03(\x0b\x32\x11.mediapipe.Anchor2T\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xff\xb8\xf3u \x01(\x0b\x32&.mediapipe.SsdAnchorsCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_formats_dot_object__detection_dot_anchor__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SSDANCHORSCALCULATOROPTIONS = _descriptor.Descriptor(
  name='SsdAnchorsCalculatorOptions',
  full_name='mediapipe.SsdAnchorsCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_size_width', full_name='mediapipe.SsdAnchorsCalculatorOptions.input_size_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_size_height', full_name='mediapipe.SsdAnchorsCalculatorOptions.input_size_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_scale', full_name='mediapipe.SsdAnchorsCalculatorOptions.min_scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_scale', full_name='mediapipe.SsdAnchorsCalculatorOptions.max_scale', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anchor_offset_x', full_name='mediapipe.SsdAnchorsCalculatorOptions.anchor_offset_x', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anchor_offset_y', full_name='mediapipe.SsdAnchorsCalculatorOptions.anchor_offset_y', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_layers', full_name='mediapipe.SsdAnchorsCalculatorOptions.num_layers', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_map_width', full_name='mediapipe.SsdAnchorsCalculatorOptions.feature_map_width', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_map_height', full_name='mediapipe.SsdAnchorsCalculatorOptions.feature_map_height', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strides', full_name='mediapipe.SsdAnchorsCalculatorOptions.strides', index=9,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aspect_ratios', full_name='mediapipe.SsdAnchorsCalculatorOptions.aspect_ratios', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reduce_boxes_in_lowest_layer', full_name='mediapipe.SsdAnchorsCalculatorOptions.reduce_boxes_in_lowest_layer', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interpolated_scale_aspect_ratio', full_name='mediapipe.SsdAnchorsCalculatorOptions.interpolated_scale_aspect_ratio', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed_anchor_size', full_name='mediapipe.SsdAnchorsCalculatorOptions.fixed_anchor_size', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multiscale_anchor_generation', full_name='mediapipe.SsdAnchorsCalculatorOptions.multiscale_anchor_generation', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_level', full_name='mediapipe.SsdAnchorsCalculatorOptions.min_level', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_level', full_name='mediapipe.SsdAnchorsCalculatorOptions.max_level', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anchor_scale', full_name='mediapipe.SsdAnchorsCalculatorOptions.anchor_scale', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(4),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scales_per_octave', full_name='mediapipe.SsdAnchorsCalculatorOptions.scales_per_octave', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalize_coordinates', full_name='mediapipe.SsdAnchorsCalculatorOptions.normalize_coordinates', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed_anchors', full_name='mediapipe.SsdAnchorsCalculatorOptions.fixed_anchors', index=20,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.SsdAnchorsCalculatorOptions.ext', index=0,
      number=247258239, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=897,
)

_SSDANCHORSCALCULATOROPTIONS.fields_by_name['fixed_anchors'].message_type = mediapipe_dot_framework_dot_formats_dot_object__detection_dot_anchor__pb2._ANCHOR
DESCRIPTOR.message_types_by_name['SsdAnchorsCalculatorOptions'] = _SSDANCHORSCALCULATOROPTIONS

SsdAnchorsCalculatorOptions = _reflection.GeneratedProtocolMessageType('SsdAnchorsCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _SSDANCHORSCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tflite.ssd_anchors_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SsdAnchorsCalculatorOptions)
  ))
_sym_db.RegisterMessage(SsdAnchorsCalculatorOptions)

_SSDANCHORSCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _SSDANCHORSCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SSDANCHORSCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
