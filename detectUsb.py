
from pysetupdi import setupdi



class detectUsb:

    def driveStatus(self):
        u = []
        devs = setupdi.devices(enumerator = "USB")

        for x in devs:
            name = x.device_class[:7]
            print(name)
            if name == "USBTest":
                u.append(x)




u = detectUsb()

u.driveStatus()
