import logging

import gpio_pb2
from config import Config
from gpio_pb2 import (GetGpioResponse, BlinkGpioResponse, SetGpioResponse)
from gpio_pb2_grpc import GpioServicer
from gpio_stub import GpioStub


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
        logging.debug('[GetGpio]: GpioNumber: %d' % request.GpioNumber)
        return GetGpioResponse(GpioNumber=request.GpioNumber,
                               State=gpio_pb2.On if self.gpio.get_gpio(request.GpioNumber) else gpio_pb2.Off)

    def SetGpio(self, request, context):
        logging.debug('[SetGpio]: GPIONumber: %d, GPIO State: %s' % (request.GpioNumber, request.State))
        self.gpio.set_gpio(request.GpioNumber, request.State == gpio_pb2.On)
        return SetGpioResponse()

    def BlinkGpio(self, request, context):
        logging.debug('[BlinkGpio]: GPIONumber: %d, Length State: %f' % (request.GpioNumber, request.Length))
        self.gpio.blink_gpio(request.GpioNumber, request.Length)
        return BlinkGpioResponse()
