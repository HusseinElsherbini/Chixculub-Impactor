import serial
import time
import socket


class EquipmentRS232(serial.Serial):

    def __init__(self, *args):
        super().__init__()
        self.connectionType = args[0]
        self.portNumber = args[1]
        self.baudRate = args[2]
        self.timeout = args[3]
        #self.channels = args[4]
        #self.addresses = args[5]
        #self.deviceType = args[6]
        self.userInput = ''
        self.ser = serial.Serial(port=self.portNumber,
                                 baudrate=self.baudRate,
                                 stopbits=serial.STOPBITS_ONE,
                                 parity=serial.PARITY_NONE,
                                 bytesize=serial.EIGHTBITS,
                                 timeout=self.timeout)
        self.out = 0
        print(self.ser.isOpen())

    def connect(self, portNumber, baudRate, timeout, deviceType):

        print('Hello! attempting to connect to {}'.format(deviceType))

        self.ser.open()
        time.sleep(.1)
        if bool(self.ser.isOpen()):
            print('Connected successfully!')
        else:
            print('Failed to connect!')

        return self.ser.isOpen()

    def send(self, userInput):

        self.userInput += "\n"
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        result = self.ser.write(self.userInput.encode())
        time.sleep(.1)
        #print(result)
        time.sleep(.1)
        return result

    def close(self):

        for x in range(self.channels):
            self.send('ADR {}'.format(x))
            self.send('OUT 0')


class EquipmentLAN(socket.socket):

    def __init__(self, *args):
        self.device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP_ADDRESS = args[0]
        self.PORT_NUMBER = args[1]
        self.DEVICE_TYPE = args[2]
        self.TIME_OUT = args[3]

    def connect(self, DEVICE_TYPE, device):

        print("Establishing connection with {}!".format(DEVICE_TYPE))
        # attempts to connect to host, if connection fails returns a timeout error
        device.connect(('169.254.4.61', 5025))
        print('Connected successfully!')
        device.settimeout(2)

    def send(self, command, device, DEVICE_TYPE):

        device.sendall(command.encode())
        time.sleep(.1)
        device.sendall('SYSTem:ERRor?\r\n'.encode())
        time.sleep(.1)
        print(DEVICE_TYPE + ':' + device.recv(1024).decode())

    def close(self, device):

        device.close()
        print("CONNECTION TERMINATED!")
        time.sleep(.1)



ard = EquipmentRS232(*["", 'COM3', 115200,  1])
while True:
    ard.send("*IDN?")
    x = ard.ser.readline()
    print(x)