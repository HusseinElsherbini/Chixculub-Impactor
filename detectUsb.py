import pyvisa
from pysetupdi import setupdi
import sys


class detectUsb:

    def driveStatus(self):
        resourceManager = pyvisa.ResourceManager()
        instrument = resourceManager.open_resource("TCPIP::169.254.202.45::INSTR")

        print(resourceManager.list_resources())

        for device in resourceManager.list_resources():
            print(device)
            dev = resourceManager.open_resource(device)
            print(dev.query('*IDN?'))


u = detectUsb()

u.driveStatus()
