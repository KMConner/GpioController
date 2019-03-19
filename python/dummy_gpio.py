from gpio_stub import GpioStub
from typing import Dict, List


class DummyGpio(GpioStub):
    def __init__(self, gpio_in: List[int]):
        self.pins: Dict[int, bool] = {}

        for num in gpio_in:
            self.pins[num] = False

    def set_gpio(self, gpio_number: int, state: bool):
        if gpio_number not in self.pins:
            raise ValueError('gpio_number is invalid!')
        self.pins[gpio_number] = state

    def get_gpio(self, gpio_number: int) -> bool:
        if gpio_number not in self.pins:
            raise ValueError('gpio_number is invalid!')
        return self.pins[gpio_number]
