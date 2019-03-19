import sys
import time
from concurrent import futures

import grpc

import config
import gpio_pb2_grpc
from config import Config
from gpioService import GpioService


def main():
    conf: Config
    try:
        conf = config.load_config('conf.json')
    except Exception as ex:
        print(ex, file=sys.stderr)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gpio_pb2_grpc.add_GpioServicer_to_server(GpioService(), server)
    server.add_insecure_port(conf.address)
    server.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()
