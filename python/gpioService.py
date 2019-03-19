import logging
import gpio_pb2
from gpio_pb2 import (GetGpioResponse, GpioState, SetGpioResponse)
from gpio_pb2_grpc import GpioServicer
from gpio_stub import GpioStub
from config import Config


class GpioService(GpioServicer):
    def __init__(self, config: Config):
        self.config = config

        self.gpio: GpioStub
        if config.debug:
            from dummy_gpio import DummyGpio
            self.gpio: GpioStub = DummyGpio(config.gpio_out)
        else:
            from gpio import Gpio
            self.gpio: GpioStub = Gpio(config.gpio_out)

    def GetGpio(self, request, context) -> GetGpioResponse:
        logging.debug('[GetGpio - Begin]: GpioNumber: %d' % request.GpioNumber)
        return GetGpioResponse(GpioNumber=request.GpioNumber,
                               State=gpio_pb2.On if self.gpio.get_gpio(request.GpioNumber) else gpio_pb2.Off)

    def SetGpio(self, request, context):
        print(request)
        self.gpio.set_gpio(request.GpioNumber, request.State == gpio_pb2.On)
        return SetGpioResponse()
