import pyvisa
from pysetupdi import setupdi
'''
rm = pyvisa.ResourceManager('@py')

print(rm.list_resources())

'''
class detectUsb:

    def driveStatus(self):
        u = []
        devs = setupdi.devices(enumerator = "USB")

        for x in devs:
            if x.device_desc == '34461A':
                print(x)
            '''
            if "USB" in x.device_class and "Hub" in x.device_class:
                u.append(x)
                print(x)
            '''


u = detectUsb()

u.driveStatus()
