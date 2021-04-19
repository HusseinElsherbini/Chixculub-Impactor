import pyvisa
from pysetupdi import setupdi
import sys
import usb.backend.libusb0
import usb.backend.libusb1
import usb.backend.openusb

class detectUsb:

    def driveStatus(self):
        resourceManager = pyvisa.ResourceManager('@py')
        #instrument = resourceManager.open_resource("TCPIP::169.254.4.61::INSTR")
        print(resourceManager.list_resources())

        for device in resourceManager.list_resources():
            print(device)




u = detectUsb()

u.driveStatus()
