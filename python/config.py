import json
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
    def gpio_out(self) -> List[int]:
        return self.__gpio_in

    @gpio_out.setter
    def gpio_out(self, gpio: List[int]):
        self.__gpio_in = gpio

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, d: bool):
        self.__debug = d


def load_config(path: str) -> Config:
    conf: dict
    with open(path, 'r') as config_file:
        conf = json.load(config_file)
    ret: Config = Config()
    ret.address = conf['address']
    ret.debug = conf['debug']
    ret.gpio_out = conf['gpio_out']
    return ret
