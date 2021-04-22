import pyvisa
from pysetupdi import setupdi
import sys

devices = []
devs = setupdi.devices()
for dev in devs:
    try:
        if dev.enumerator_name == "USB":
            if dev.device_class == "Bluetooth" or dev.device_class == "HIDClass" or dev.device_class == "Net" or dev.device_class == "MEDIA":
                pass
            elif "HUB" in dev.manufacturer or "Controller" in dev.manufacturer or "storage" in dev.manufacturer:
                print(dev.manufacturer)
                pass
            else:
                devices.append(dev)

    except (KeyError,AttributeError,):
        continue

print("\n")
for x in devices:
    try:
        print("Device name: {}   Device class: {}".format(x,x.device_class))
    except AttributeError:
        pass
class detectUsb:

    def driveStatus(self):
        resourceManager = pyvisa.ResourceManager()
        #instrument = resourceManager.open_resource("TCPIP::169.254.202.45::INSTR")

        print(resourceManager.list_resources())

        for device in resourceManager.list_resources():
            print(device)
            dev = resourceManager.open_resource(device)
            print(dev.query('*IDN?'))


u = detectUsb()

#u.driveStatus()
