# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/pose_detector/proto/pose_detector_graph_options.proto

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
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/vision/pose_detector/proto/pose_detector_graph_options.proto',
  package='mediapipe.tasks.vision.pose_detector.proto',
  syntax='proto2',
  serialized_pb=_b('\nOmediapipe/tasks/cc/vision/pose_detector/proto/pose_detector_graph_options.proto\x12*mediapipe.tasks.vision.pose_detector.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xb0\x02\n\x18PoseDetectorGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12%\n\x18min_detection_confidence\x18\x02 \x01(\x02:\x03\x30.5\x12&\n\x19min_suppression_threshold\x18\x03 \x01(\x02:\x03\x30.5\x12\x11\n\tnum_poses\x18\x04 \x01(\x05\x32s\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x9d\xae\xbb\xf5\x01 \x01(\x0b\x32\x44.mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptionsBU\n4com.google.mediapipe.tasks.vision.posedetector.protoB\x1dPoseDetectorGraphOptionsProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POSEDETECTORGRAPHOPTIONS = _descriptor.Descriptor(
  name='PoseDetectorGraphOptions',
  full_name='mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_detection_confidence', full_name='mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptions.min_detection_confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_suppression_threshold', full_name='mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptions.min_suppression_threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_poses', full_name='mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptions.num_poses', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptions.ext', index=0,
      number=514774813, type=11, cpp_type=10, label=1,
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
  serialized_start=262,
  serialized_end=566,
)

_POSEDETECTORGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
DESCRIPTOR.message_types_by_name['PoseDetectorGraphOptions'] = _POSEDETECTORGRAPHOPTIONS

PoseDetectorGraphOptions = _reflection.GeneratedProtocolMessageType('PoseDetectorGraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _POSEDETECTORGRAPHOPTIONS,
  __module__ = 'mediapipe.tasks.cc.vision.pose_detector.proto.pose_detector_graph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.pose_detector.proto.PoseDetectorGraphOptions)
  ))
_sym_db.RegisterMessage(PoseDetectorGraphOptions)

_POSEDETECTORGRAPHOPTIONS.extensions_by_name['ext'].message_type = _POSEDETECTORGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_POSEDETECTORGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n4com.google.mediapipe.tasks.vision.posedetector.protoB\035PoseDetectorGraphOptionsProto'))
# @@protoc_insertion_point(module_scope)
