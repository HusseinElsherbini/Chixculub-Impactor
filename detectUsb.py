import pyvisa
from pysetupdi import setupdi
import usb.core
import usb.backend.libusb1
import sys
import usbtmc

devices = []
devices_VID_PID = []
devs = setupdi.devices()

for dev in devs:
    try:
        if dev.enumerator_name == "USB":
            if dev.device_class == "Bluetooth" or dev.device_class == "HIDClass" or dev.device_class == "Net" or dev.device_class == "MEDIA":
                pass
            elif "HUB" in dev.manufacturer or "Hub" in dev.device_desc or "Controller" in dev.manufacturer or "storage" in dev.manufacturer:
                # print(dev.manufacturer)
                pass
            else:
                devices.append(dev)

    except (KeyError, AttributeError,):
        continue

print("\n")
for x in devices:
    try:
        print("Device name: {}   Device class: {}".format(x, x.manufacturer))
        h = x.hardware_id
        devices_VID_PID.append(("0x"+h[1][8:12], "0x"+h[1][17:]))

    except AttributeError:
        pass

print(devices_VID_PID)


class device:

    def __init__(self, vid, pid):

        self.VID = vid
        self.PID = pid
        self.dev = usbtmc.list_devices()


    def driveStatus(self):
        resourceManager = pyvisa.ResourceManager()
        # instrument = resourceManager.open_resource("TCPIP::169.254.202.45::INSTR")

        print(resourceManager.list_resources())

        for device in resourceManager.list_resources():
            print(device)
            dev = resourceManager.open_resource(device)
            #print(dev.query('*IDN?'))


u = device(devices_VID_PID[1][0], devices_VID_PID[1][1])
u.driveStatus()
print(u.dev)
