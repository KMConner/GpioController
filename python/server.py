from gpioService import GpioService
import grpc
from concurrent import futures
import gpio_pb2_grpc
import time


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gpio_pb2_grpc.add_GpioServicer_to_server(GpioService(), server)
    server.add_insecure_port('[::]:8081')
    server.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()
