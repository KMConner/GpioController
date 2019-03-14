from gpio_pb2_grpc import GpioServicer
from gpio_pb2 import GetGpioRequest, GetGpioResponse, GpioState, SetGpioResponse
import gpio_pb2


class GpioService(GpioServicer):
    def GetGpio(self, request: GetGpioRequest, context) -> GetGpioResponse:
        print(request)
        return GetGpioResponse(GpioNumber=request.GpioNumber, State=gpio_pb2.On)

    def SetGpio(self, request, context):
        print(request)
        return SetGpioResponse()
