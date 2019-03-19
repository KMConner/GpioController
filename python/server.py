import logging
import sys
import time
from concurrent import futures

import grpc

import config
import gpio_pb2_grpc
from config import Config
from gpioService import GpioService


def main():
    # configure logging
    LOG_FORMAT = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='./log/ex.log',
                        level=logging.DEBUG, format=LOG_FORMAT)

    logging.debug('Server Starting...')

    conf: Config
    try:
        conf = config.load_config('conf.json')
    except Exception as ex:
        print('Failed to load sever configuration.', file=sys.stderr)
        print(ex, file=sys.stderr)
        exit(1)

    if conf.debug:
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter(LOG_FORMAT))
        console.setLevel(logging.DEBUG)
        logging.getLogger().addHandler(console)

    logging.debug(conf)

    # Start server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gpio_pb2_grpc.add_GpioServicer_to_server(GpioService(conf), server)
    server.add_insecure_port(conf.address)
    server.start()
    logging.info('Server started.')

    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)
        logging.info('Server stopped')


if __name__ == '__main__':
    main()
