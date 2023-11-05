# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/calculator_profile.proto

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
  name='mediapipe/framework/calculator_profile.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n,mediapipe/framework/calculator_profile.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"o\n\rTimeHistogram\x12\x10\n\x05total\x18\x01 \x01(\x03:\x01\x30\x12#\n\x12interval_size_usec\x18\x02 \x01(\x03:\x07\x31\x30\x30\x30\x30\x30\x30\x12\x18\n\rnum_intervals\x18\x03 \x01(\x03:\x01\x31\x12\r\n\x05\x63ount\x18\x04 \x03(\x03\"b\n\rStreamProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\tback_edge\x18\x02 \x01(\x08:\x05\x66\x61lse\x12)\n\x07latency\x18\x03 \x01(\x0b\x32\x18.mediapipe.TimeHistogram\"\xb3\x02\n\x11\x43\x61lculatorProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0copen_runtime\x18\x02 \x01(\x03:\x01\x30\x12\x18\n\rclose_runtime\x18\x03 \x01(\x03:\x01\x30\x12\x31\n\x0fprocess_runtime\x18\x04 \x01(\x0b\x32\x18.mediapipe.TimeHistogram\x12\x37\n\x15process_input_latency\x18\x05 \x01(\x0b\x32\x18.mediapipe.TimeHistogram\x12\x38\n\x16process_output_latency\x18\x06 \x01(\x0b\x32\x18.mediapipe.TimeHistogram\x12\x37\n\x15input_stream_profiles\x18\x07 \x03(\x0b\x32\x18.mediapipe.StreamProfile\"\xe1\x07\n\nGraphTrace\x12\x11\n\tbase_time\x18\x01 \x01(\x03\x12\x16\n\x0e\x62\x61se_timestamp\x18\x02 \x01(\x03\x12\x17\n\x0f\x63\x61lculator_name\x18\x03 \x03(\t\x12\x13\n\x0bstream_name\x18\x04 \x03(\t\x12?\n\x10\x63\x61lculator_trace\x18\x05 \x03(\x0b\x32%.mediapipe.GraphTrace.CalculatorTrace\x1a\x8e\x01\n\x0bStreamTrace\x12\x12\n\nstart_time\x18\x01 \x01(\x03\x12\x13\n\x0b\x66inish_time\x18\x02 \x01(\x03\x12\x18\n\x10packet_timestamp\x18\x03 \x01(\x03\x12\x11\n\tstream_id\x18\x04 \x01(\x05\x12\x15\n\tpacket_id\x18\x05 \x01(\x03\x42\x02\x18\x01\x12\x12\n\nevent_data\x18\x06 \x01(\x03\x1a\x9d\x02\n\x0f\x43\x61lculatorTrace\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x17\n\x0finput_timestamp\x18\x02 \x01(\x03\x12\x33\n\nevent_type\x18\x03 \x01(\x0e\x32\x1f.mediapipe.GraphTrace.EventType\x12\x12\n\nstart_time\x18\x04 \x01(\x03\x12\x13\n\x0b\x66inish_time\x18\x05 \x01(\x03\x12\x36\n\x0binput_trace\x18\x06 \x03(\x0b\x32!.mediapipe.GraphTrace.StreamTrace\x12\x37\n\x0coutput_trace\x18\x07 \x03(\x0b\x32!.mediapipe.GraphTrace.StreamTrace\x12\x11\n\tthread_id\x18\x08 \x01(\x05\"\x87\x03\n\tEventType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\x0b\n\x07PROCESS\x10\x02\x12\t\n\x05\x43LOSE\x10\x03\x12\r\n\tNOT_READY\x10\x04\x12\x15\n\x11READY_FOR_PROCESS\x10\x05\x12\x13\n\x0fREADY_FOR_CLOSE\x10\x06\x12\r\n\tTHROTTLED\x10\x07\x12\x0f\n\x0bUNTHROTTLED\x10\x08\x12\x11\n\rCPU_TASK_USER\x10\t\x12\x13\n\x0f\x43PU_TASK_SYSTEM\x10\n\x12\x0c\n\x08GPU_TASK\x10\x0b\x12\x0c\n\x08\x44SP_TASK\x10\x0c\x12\x0c\n\x08TPU_TASK\x10\r\x12\x13\n\x0fGPU_CALIBRATION\x10\x0e\x12\x11\n\rPACKET_QUEUED\x10\x0f\x12\x13\n\x0fGPU_TASK_INVOKE\x10\x10\x12\x13\n\x0fTPU_TASK_INVOKE\x10\x11\x12\x13\n\x0f\x43PU_TASK_INVOKE\x10\x12\x12\x1c\n\x18GPU_TASK_INVOKE_ADVANCED\x10\x13\x12\x19\n\x15TPU_TASK_INVOKE_ASYNC\x10\x14\"\xa7\x01\n\x0cGraphProfile\x12*\n\x0bgraph_trace\x18\x01 \x03(\x0b\x32\x15.mediapipe.GraphTrace\x12\x39\n\x13\x63\x61lculator_profiles\x18\x02 \x03(\x0b\x32\x1c.mediapipe.CalculatorProfile\x12\x30\n\x06\x63onfig\x18\x03 \x01(\x0b\x32 .mediapipe.CalculatorGraphConfigB4\n\x1a\x63om.google.mediapipe.protoB\x16\x43\x61lculatorProfileProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GRAPHTRACE_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='mediapipe.GraphTrace.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_READY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_FOR_PROCESS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_FOR_CLOSE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THROTTLED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNTHROTTLED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPU_TASK_USER', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPU_TASK_SYSTEM', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU_TASK', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DSP_TASK', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPU_TASK', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU_CALIBRATION', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PACKET_QUEUED', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU_TASK_INVOKE', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPU_TASK_INVOKE', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPU_TASK_INVOKE', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPU_TASK_INVOKE_ADVANCED', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPU_TASK_INVOKE_ASYNC', index=20, number=20,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1223,
  serialized_end=1614,
)
_sym_db.RegisterEnumDescriptor(_GRAPHTRACE_EVENTTYPE)


_TIMEHISTOGRAM = _descriptor.Descriptor(
  name='TimeHistogram',
  full_name='mediapipe.TimeHistogram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='mediapipe.TimeHistogram.total', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interval_size_usec', full_name='mediapipe.TimeHistogram.interval_size_usec', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=1000000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_intervals', full_name='mediapipe.TimeHistogram.num_intervals', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='mediapipe.TimeHistogram.count', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
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
  serialized_start=97,
  serialized_end=208,
)


_STREAMPROFILE = _descriptor.Descriptor(
  name='StreamProfile',
  full_name='mediapipe.StreamProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mediapipe.StreamProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='back_edge', full_name='mediapipe.StreamProfile.back_edge', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latency', full_name='mediapipe.StreamProfile.latency', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
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
  serialized_start=210,
  serialized_end=308,
)


_CALCULATORPROFILE = _descriptor.Descriptor(
  name='CalculatorProfile',
  full_name='mediapipe.CalculatorProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mediapipe.CalculatorProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_runtime', full_name='mediapipe.CalculatorProfile.open_runtime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close_runtime', full_name='mediapipe.CalculatorProfile.close_runtime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_runtime', full_name='mediapipe.CalculatorProfile.process_runtime', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_input_latency', full_name='mediapipe.CalculatorProfile.process_input_latency', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_output_latency', full_name='mediapipe.CalculatorProfile.process_output_latency', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_stream_profiles', full_name='mediapipe.CalculatorProfile.input_stream_profiles', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
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
  serialized_start=311,
  serialized_end=618,
)


_GRAPHTRACE_STREAMTRACE = _descriptor.Descriptor(
  name='StreamTrace',
  full_name='mediapipe.GraphTrace.StreamTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='mediapipe.GraphTrace.StreamTrace.start_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish_time', full_name='mediapipe.GraphTrace.StreamTrace.finish_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packet_timestamp', full_name='mediapipe.GraphTrace.StreamTrace.packet_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='mediapipe.GraphTrace.StreamTrace.stream_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packet_id', full_name='mediapipe.GraphTrace.StreamTrace.packet_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='event_data', full_name='mediapipe.GraphTrace.StreamTrace.event_data', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
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
  serialized_start=790,
  serialized_end=932,
)

_GRAPHTRACE_CALCULATORTRACE = _descriptor.Descriptor(
  name='CalculatorTrace',
  full_name='mediapipe.GraphTrace.CalculatorTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='mediapipe.GraphTrace.CalculatorTrace.node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_timestamp', full_name='mediapipe.GraphTrace.CalculatorTrace.input_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='mediapipe.GraphTrace.CalculatorTrace.event_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='mediapipe.GraphTrace.CalculatorTrace.start_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish_time', full_name='mediapipe.GraphTrace.CalculatorTrace.finish_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_trace', full_name='mediapipe.GraphTrace.CalculatorTrace.input_trace', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_trace', full_name='mediapipe.GraphTrace.CalculatorTrace.output_trace', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='mediapipe.GraphTrace.CalculatorTrace.thread_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
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
  serialized_start=935,
  serialized_end=1220,
)

_GRAPHTRACE = _descriptor.Descriptor(
  name='GraphTrace',
  full_name='mediapipe.GraphTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_time', full_name='mediapipe.GraphTrace.base_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_timestamp', full_name='mediapipe.GraphTrace.base_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculator_name', full_name='mediapipe.GraphTrace.calculator_name', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream_name', full_name='mediapipe.GraphTrace.stream_name', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculator_trace', full_name='mediapipe.GraphTrace.calculator_trace', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GRAPHTRACE_STREAMTRACE, _GRAPHTRACE_CALCULATORTRACE, ],
  enum_types=[
    _GRAPHTRACE_EVENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=1614,
)


_GRAPHPROFILE = _descriptor.Descriptor(
  name='GraphProfile',
  full_name='mediapipe.GraphProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph_trace', full_name='mediapipe.GraphProfile.graph_trace', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculator_profiles', full_name='mediapipe.GraphProfile.calculator_profiles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config', full_name='mediapipe.GraphProfile.config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
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
  serialized_start=1617,
  serialized_end=1784,
)

_STREAMPROFILE.fields_by_name['latency'].message_type = _TIMEHISTOGRAM
_CALCULATORPROFILE.fields_by_name['process_runtime'].message_type = _TIMEHISTOGRAM
_CALCULATORPROFILE.fields_by_name['process_input_latency'].message_type = _TIMEHISTOGRAM
_CALCULATORPROFILE.fields_by_name['process_output_latency'].message_type = _TIMEHISTOGRAM
_CALCULATORPROFILE.fields_by_name['input_stream_profiles'].message_type = _STREAMPROFILE
_GRAPHTRACE_STREAMTRACE.containing_type = _GRAPHTRACE
_GRAPHTRACE_CALCULATORTRACE.fields_by_name['event_type'].enum_type = _GRAPHTRACE_EVENTTYPE
_GRAPHTRACE_CALCULATORTRACE.fields_by_name['input_trace'].message_type = _GRAPHTRACE_STREAMTRACE
_GRAPHTRACE_CALCULATORTRACE.fields_by_name['output_trace'].message_type = _GRAPHTRACE_STREAMTRACE
_GRAPHTRACE_CALCULATORTRACE.containing_type = _GRAPHTRACE
_GRAPHTRACE.fields_by_name['calculator_trace'].message_type = _GRAPHTRACE_CALCULATORTRACE
_GRAPHTRACE_EVENTTYPE.containing_type = _GRAPHTRACE
_GRAPHPROFILE.fields_by_name['graph_trace'].message_type = _GRAPHTRACE
_GRAPHPROFILE.fields_by_name['calculator_profiles'].message_type = _CALCULATORPROFILE
_GRAPHPROFILE.fields_by_name['config'].message_type = mediapipe_dot_framework_dot_calculator__pb2._CALCULATORGRAPHCONFIG
DESCRIPTOR.message_types_by_name['TimeHistogram'] = _TIMEHISTOGRAM
DESCRIPTOR.message_types_by_name['StreamProfile'] = _STREAMPROFILE
DESCRIPTOR.message_types_by_name['CalculatorProfile'] = _CALCULATORPROFILE
DESCRIPTOR.message_types_by_name['GraphTrace'] = _GRAPHTRACE
DESCRIPTOR.message_types_by_name['GraphProfile'] = _GRAPHPROFILE

TimeHistogram = _reflection.GeneratedProtocolMessageType('TimeHistogram', (_message.Message,), dict(
  DESCRIPTOR = _TIMEHISTOGRAM,
  __module__ = 'mediapipe.framework.calculator_profile_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TimeHistogram)
  ))
_sym_db.RegisterMessage(TimeHistogram)

StreamProfile = _reflection.GeneratedProtocolMessageType('StreamProfile', (_message.Message,), dict(
  DESCRIPTOR = _STREAMPROFILE,
  __module__ = 'mediapipe.framework.calculator_profile_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.StreamProfile)
  ))
_sym_db.RegisterMessage(StreamProfile)

CalculatorProfile = _reflection.GeneratedProtocolMessageType('CalculatorProfile', (_message.Message,), dict(
  DESCRIPTOR = _CALCULATORPROFILE,
  __module__ = 'mediapipe.framework.calculator_profile_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.CalculatorProfile)
  ))
_sym_db.RegisterMessage(CalculatorProfile)

GraphTrace = _reflection.GeneratedProtocolMessageType('GraphTrace', (_message.Message,), dict(

  StreamTrace = _reflection.GeneratedProtocolMessageType('StreamTrace', (_message.Message,), dict(
    DESCRIPTOR = _GRAPHTRACE_STREAMTRACE,
    __module__ = 'mediapipe.framework.calculator_profile_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.GraphTrace.StreamTrace)
    ))
  ,

  CalculatorTrace = _reflection.GeneratedProtocolMessageType('CalculatorTrace', (_message.Message,), dict(
    DESCRIPTOR = _GRAPHTRACE_CALCULATORTRACE,
    __module__ = 'mediapipe.framework.calculator_profile_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.GraphTrace.CalculatorTrace)
    ))
  ,
  DESCRIPTOR = _GRAPHTRACE,
  __module__ = 'mediapipe.framework.calculator_profile_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.GraphTrace)
  ))
_sym_db.RegisterMessage(GraphTrace)
_sym_db.RegisterMessage(GraphTrace.StreamTrace)
_sym_db.RegisterMessage(GraphTrace.CalculatorTrace)

GraphProfile = _reflection.GeneratedProtocolMessageType('GraphProfile', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHPROFILE,
  __module__ = 'mediapipe.framework.calculator_profile_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.GraphProfile)
  ))
_sym_db.RegisterMessage(GraphProfile)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.google.mediapipe.protoB\026CalculatorProfileProto'))
_GRAPHTRACE_STREAMTRACE.fields_by_name['packet_id'].has_options = True
_GRAPHTRACE_STREAMTRACE.fields_by_name['packet_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
