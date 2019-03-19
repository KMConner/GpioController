from typing import List

from gpio_stub import GpioStub


class Gpio(GpioStub):
    def __init__(self, gpio_in: List[int]):
        pass

    def set_gpio(self, gpio_number: int, state: bool):
        raise NotImplementedError()

    def get_gpio(self, gpio_number: int) -> bool:
        raise NotImplementedError()
