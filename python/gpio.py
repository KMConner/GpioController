from typing import Dict, List

from gpiozero import LED

from gpio_stub import GpioStub


class Gpio(GpioStub):
    def __init__(self, gpio_in: List[int]):
        super().__init__(gpio_in)
        self.led: Dict[int, LED] = {}

        for gpio in gpio_in:
            self.led[gpio] = LED(gpio)

    def set_gpio(self, gpio_number: int, state: bool) -> None:
        self._check_number(gpio_number)
        self.led[gpio_number].value = 1 if state else 0

    def get_gpio(self, gpio_number: int) -> bool:
        self._check_number(gpio_number)
        return False if self.led[gpio_number] == 0 else True

    def _check_number(self, num: int):
        if num not in self.led:
            raise ValueError()
