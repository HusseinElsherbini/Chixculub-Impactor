import serial
import time
import socket


class EquipmentRS232(serial.Serial):

    def __init__(self, *args):
        super().__init__()
        self.portNumber = args[0]
        self.baudRate = args[1]
        self.timeout = args[2]
        #self.channels = args[4]
        #self.addresses = args[5]
        #self.deviceType = args[6]
        self.userInput = ''

        self.connect()

    def connect(self):

        try:
            # sets up a serial object with given parameters and tries to open the communication port
            print("Attempting communication with power supply..")

            self.ser = serial.Serial(port=self.portNumber,
                                     baudrate=self.baudRate,
                                     stopbits=serial.STOPBITS_ONE,
                                     parity=serial.PARITY_NONE,
                                     bytesize=serial.EIGHTBITS,
                                     timeout=self.timeout)

            self.ser.isOpen()
            print('port opened successfully')

        except IOError:
            # if port is already opened, close it and open it again
            self.ser.close()
            self.ser.open()
            print('port was already open, was closed and opened again')

    def send(self, userInput):
        #userinput = userInput.strip()
        userInput += "\r\n"
        self.ser.write(userInput.encode())
        #time.sleep(.2)
        return self.ser.readline().decode()

    def send_without_read(self, input):
        self.userInput += "\r\n"
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.write(self.userInput.encode())

    def close(self):

        self.ser.close()


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




"""
u.ser.write("ADR 6\r\n".encode())
print(u.ser.readline().decode())

u.ser.write("IDN?\r\n".encode())
print(u.ser.readline().decode())
"""