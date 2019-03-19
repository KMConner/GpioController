from typing import List


class Config:
    def __init__(self):
        self.__address: str
        self.__gpio_in: List[int]
        self.__debug: bool = False

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, addr: str):
        self.__address = addr

    @property
    def gpio_in(self) -> List[int]:
        return self.__gpio_in

    @gpio_in.setter
    def gpio_in(self, gpio: List[int]):
        self.__gpio_in = gpio

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, d: bool):
        self.__debug = d


def load_config(path: str) -> Config:
    pass
