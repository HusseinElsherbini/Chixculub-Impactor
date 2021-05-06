import pyvisa
from pyvisa import attributes, constants
import sys
import threading
import time
from pysetupdi import setupdi
import serial.tools.list_ports as portsList

class initDevice:

    def __init__(self):


        self.devices = {}
        self.connectedDevices = []


    def updateDevicesDB(self,device, present=False):

        try:
            if present:
                self.devices[device]['Resource'].open()
                return
            dev = self.resourceManager.open_resource(device)
            self.devices.update({str(dev.resource_name)[8:12] + str(dev.resource_name)[16:20]: {
            'Model Name': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_MODEL_NAME),
            'Device type': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_RSRC_CLASS),
            'Connection Type': str(dev.interface_type)[14:],
            'Visa Handle': device,
            'Resource': dev
            }})

        except Exception as e:
            print(e)



    def detectDevices(self):

        self.resourceManager = pyvisa.ResourceManager()
        for device in self.resourceManager.list_resources():
            print(str(device))
            try:


                if "ASRL" in str(device):
                    dev = self.resourceManager.open_resource(device, baud_rate=115200)

                    devs = setupdi.devices(enumerator="USB")
                    x = [port[0] for port in list(portsList.comports())]

                    for COM in devs:
                        if 'COM'+ str(device).rsplit("::")[0][4:] in str(COM):
                            h = COM.hardware_id
                            h= h[1][8:12] + h[1][17:]
                            break

                    self.devices.update({h: {
                        'Model Name': 'Device' + ' (COM'+ str(device).rsplit("::")[0][4:] + ')',
                        'Device Type': 'COM'+ str(device).rsplit("::")[0][4:] if 'COM' + str(device).rsplit("::")[0][4:] in x else 'PORT_ERROR',
                        'Connection Type': 'Serial',
                        'Visa Handle': device,
                        'Resource': dev
                    }})

                elif "USB" in str(device):
                    dev = self.resourceManager.open_resource(device)
                    self.devices.update({str(device)[8:12] + str(device)[16:20]: {
                        'Model Name': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_MODEL_NAME),
                        'Device type': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_RSRC_CLASS),
                        'Connection Type': str(dev.interface_type)[14:],
                        'Visa Handle': device,
                        'Resource': dev
                    }})


            except Exception as e:
                print(self.devices)
                print(e)



    def startThread(self, function, arguments):

        self.threadx = threading.Thread(target=function, args=arguments)
        self.threadx.daemon = True
        self.threadx.start()

    def vidValidator(self):
        devices = []
        devices_VID_PID = []
        devs = setupdi.devices(enumerator="USB")

        for dev in devs:

            try:
                if "USB Test and Measurement" in str(dev):
                    devices.append(dev)
                elif "Ports" in dev.device_class:
                    devices.append(dev)
            except (KeyError, AttributeError,):
                continue

        for x in devices:
            try:
                h = x.hardware_id
                devices_VID_PID.append( h[1][8:12] + h[1][17:])

            except AttributeError:
                pass
        return devices_VID_PID

class device:

    def __init__(self, args):

        self.deviceName = args[0]
        self.VID_PID = args[1]
        self.modelName = args[2]

        pass

    def open(self):

        pass

"""
u = initDevice()
u.detectDevices()

while True:
    print(u.resourceManager.list_resources())
    print(u.vidValidator())
    if len(u.resourceManager.list_resources()) != 0:
        break
    time.sleep(1)
while True:
    dev = u.resourceManager.open_resource(u.resourceManager.list_resources()[0])
    print(dev.query("*IDN?"))
    time.sleep(2)
#print(u.devices)
"""

