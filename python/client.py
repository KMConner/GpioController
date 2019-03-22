from gpio_pb2_grpc import GpioStub
import grpc
import gpio_pb2
from gpio_pb2 import GetGpioRequest, GetGpioResponse, GpioState, SetGpioRequest, BlinkGpioRequest
import sys

USAGE_STR = """
Usage:
  python client.py <command> [<args>]

  get   Gets the input of GPIO.
  set   Sets the output of GPIO.

Examples:

  python client.py set 10 On  
  python client.py set 17 Off
  python client.py get 10  
"""


def main():
    arg_length = len(sys.argv)

    if arg_length < 3:
        print(USAGE_STR)
        return

    command_name = sys.argv[1]
    gpio_number = int(sys.argv[2])

    if command_name == 'set':
        if arg_length != 4:
            print(USAGE_STR)
            return
        if sys.argv[3] != 'On' and sys.argv[3] != 'Off':
            print(USAGE_STR)
            return
    elif command_name == 'get':
        if arg_length != 3:
            print(USAGE_STR)
            return
    elif command_name == 'blink':
        if arg_length != 4:
            print(USAGE_STR)
            return
    else:
        print(USAGE_STR)
        return

    with grpc.insecure_channel('127.0.0.1:8081') as channel:
        stub = GpioStub(channel)
        if command_name == 'get':
            resp = stub.GetGpio(GetGpioRequest(GpioNumber=gpio_number))
            print(resp)
        elif command_name == 'set':
            resp = stub.SetGpio(SetGpioRequest(GpioNumber=gpio_number,
                                               State=gpio_pb2.On
                                               if sys.argv[3] == 'On'
                                               else gpio_pb2.Off))
            print("Success!")
        elif command_name == 'blink':
            stub.BlinkGpio(BlinkGpioRequest(GpioNumber=gpio_number, Length=float(sys.argv[3])))
            print("Success!")


if __name__ == "__main__":
    main()
