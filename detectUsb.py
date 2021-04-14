from winrt.windows.devices import usb


class detectUsb:

    def driveStatus(self):
        u = usb.UsbDeviceClasses
        print(u)


u = detectUsb()

u.driveStatus()