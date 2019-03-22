# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import gpio_pb2 as gpio__pb2


class GpioStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetGpio = channel.unary_unary(
        '/Gpio/GetGpio',
        request_serializer=gpio__pb2.GetGpioRequest.SerializeToString,
        response_deserializer=gpio__pb2.GetGpioResponse.FromString,
        )
    self.SetGpio = channel.unary_unary(
        '/Gpio/SetGpio',
        request_serializer=gpio__pb2.SetGpioRequest.SerializeToString,
        response_deserializer=gpio__pb2.SetGpioResponse.FromString,
        )
    self.BlinkGpio = channel.unary_unary(
        '/Gpio/BlinkGpio',
        request_serializer=gpio__pb2.BlinkGpioRequest.SerializeToString,
        response_deserializer=gpio__pb2.BlinkGpioResponse.FromString,
        )


class GpioServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetGpio(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetGpio(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BlinkGpio(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GpioServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetGpio': grpc.unary_unary_rpc_method_handler(
          servicer.GetGpio,
          request_deserializer=gpio__pb2.GetGpioRequest.FromString,
          response_serializer=gpio__pb2.GetGpioResponse.SerializeToString,
      ),
      'SetGpio': grpc.unary_unary_rpc_method_handler(
          servicer.SetGpio,
          request_deserializer=gpio__pb2.SetGpioRequest.FromString,
          response_serializer=gpio__pb2.SetGpioResponse.SerializeToString,
      ),
      'BlinkGpio': grpc.unary_unary_rpc_method_handler(
          servicer.BlinkGpio,
          request_deserializer=gpio__pb2.BlinkGpioRequest.FromString,
          response_serializer=gpio__pb2.BlinkGpioResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Gpio', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
