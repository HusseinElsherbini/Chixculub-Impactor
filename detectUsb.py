from winrt.windows.devices.enumeration import DeviceInformation
from winrt.windows.devices.usb import UsbDevice
from winrt.windows.devices import usb
from winrt import *

class detectUsb:

    def driveStatus(self):
        #u =
        #print(u)
        print(DeviceInformation.find_all_async(UsbDevice.get_device_class_selector(usb.UsbDeviceClasses.cdc)))

u = detectUsb()

u.driveStatus()