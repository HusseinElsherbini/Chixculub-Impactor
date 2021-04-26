import pyvisa
from pyvisa import attributes
import sys
import threading
import time
from pysetupdi import setupdi


class initDevice:

    def __init__(self):

        self.resourceManager = pyvisa.ResourceManager()
        self.devices = {}
        self.connectedDevices = []
        self.detectDevices()



    def deviceStatus(self):

        print(self.resourceManager.list_resources())
        d = self.vidValidator()
        while True:
            for device in self.resourceManager.list_resources():
                try:
                    if str(device)[8:12] + str(device)[16:20] in d:
                        if str(device)[8:12] + str(device)[16:20] not in self.devices.keys():
                            self.updateDevicesDB(device)
                        if self.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'] not in self.connectedDevices:
                            self.connectedDevices.append(self.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'])
                    else:
                        print(self.devices)
                        try:
                            if self.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'] in self.connectedDevices:
                                self.connectedDevices.remove(self.devices[str(device)[8:12] + str(device)[16:20]]['Model Name'])
                        except KeyError:
                            pass


                except pyvisa.errors.VisaIOError:
                    pass
            print(self.connectedDevices)
            break
            time.sleep(2)

    def updateDevicesDB(self,device):
        dev = self.resourceManager.open_resource(device)
        self.devices.update({str(device)[8:12] + str(device)[16:20]: {
            'Model Name': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_MODEL_NAME),
            'Device type': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_RSRC_CLASS),
            'Connection Type': str(dev.interface_type)[14:],
        }})

    def detectDevices(self):
        i = 1
        for device in self.resourceManager.list_resources():

            try:
                dev = self.resourceManager.open_resource(device)

                dev.timeout = 100
                self.devices.update({str(device)[8:12] + str(device)[16:20]: {
                    'Model Name': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_MODEL_NAME),
                    'Device type': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_RSRC_CLASS),
                    'Connection Type': str(dev.interface_type)[14:],
                }})
                #print(dev.query("*IDN?"))
                i += 1
            except pyvisa.errors.VisaIOError:
                try:
                    #print(dev.last_status)
                    self.devices[str(device)[8:12] + str(device)[16:20]].update(({'timeoutError': True}))
                    i += 1
                except KeyError:
                    pass
            try:
                dev.close()

            except UnboundLocalError:
                pass
        print(self.devices)

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

            except (KeyError, AttributeError,):
                continue

        for x in devices:
            try:
                h = x.hardware_id
                devices_VID_PID.append( h[1][8:12] + h[1][17:])

            except AttributeError:
                pass
        return devices_VID_PID

class device(pyvisa.resources.Resource):

    def __init__(self, parent=None):
        super.__init__(parent)


u = initDevice()
u.deviceStatus()
#u.vidValidator()
