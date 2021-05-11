import pyvisa
from pyvisa import attributes
import threading
from pysetupdi import setupdi
import serial.tools.list_ports as portsList
import equipment
import sys
import os

class initDevice:
    devices = {}
    connectedDevices = []

    def __init__(self):
        self.resourceManager = pyvisa.ResourceManager()


    def updateDevicesDB(self,device,devName="",visaHandle="", present=False):

        try:
            if present:
                if "COM" in initDevice.devices[device]['Model Name']:
                    initDevice.devices[device]['Resource'].connect()
                else:
                    initDevice.devices[device]['Resource'].open()
                return
            if "COM" in devName:

                initDevice.devices.update({device: {
                    'Model Name': 'Device' + ' (COM' + str(visaHandle).rsplit("::")[0][4:] + ')',
                    'Device Type': 'COM' + str(visaHandle).rsplit("::")[0][4:],
                    'Connection Type': 'Serial',
                    'Visa Handle': visaHandle,
                    'Script Status': 'Inactive',
                    'Resource': equipment.EquipmentRS232(*['COM'+ str(device).rsplit("::")[0][4:],'9600',0.1])
                    }})
                return
            dev = self.resourceManager.open_resource(device)
            initDevice.devices.update({str(dev.resource_name)[8:12] + str(dev.resource_name)[16:20]: {
            'Model Name': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_MODEL_NAME),
            'Device type': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_RSRC_CLASS),
            'Connection Type': str(dev.interface_type)[14:],
            'Visa Handle': device,
            'Script Status': 'Inactive',
            'Resource': dev
            }})

        except Exception as e:
            #print(str(e)  + ' {{initDevice, updateDevicesDB, line 44}}')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(str(e) + ' {{{}, {}, {}}}'.format(exc_type, exc_obj, exc_tb))




    def detectDevices(self):

        #self.resourceManager = pyvisa.ResourceManager()
        for device in self.resourceManager.list_resources():

            try:


                if "ASRL" in str(device):
                    #dev = self.resourceManager.open_resource(device)
                    #dev =
                    devs = setupdi.devices(enumerator="USB")
                    x = [port[0] for port in list(portsList.comports())]

                    for COM in devs:
                        if 'COM'+ str(device).rsplit("::")[0][4:] in str(COM):
                            h = COM.hardware_id
                            h= h[1][8:12] + h[1][17:]
                            break

                    initDevice.devices.update({h: {
                        'Model Name': 'Device' + ' (COM'+ str(device).rsplit("::")[0][4:] + ')',
                        'Device Type': 'COM'+ str(device).rsplit("::")[0][4:] if 'COM' + str(device).rsplit("::")[0][4:] in x else 'PORT_ERROR',
                        'Connection Type': 'Serial',
                        'Visa Handle': device,
                        'Script Status': 'Inactive',
                        'Resource': equipment.EquipmentRS232(*['COM'+ str(device).rsplit("::")[0][4:],'9600',0.1])
                    }})

                elif "USB" in str(device):
                    dev = self.resourceManager.open_resource(device)
                    initDevice.devices.update({str(device)[8:12] + str(device)[16:20]: {
                        'Model Name': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_MODEL_NAME),
                        'Device type': dev.get_visa_attribute(pyvisa.attributes.constants.VI_ATTR_RSRC_CLASS),
                        'Connection Type': str(dev.interface_type)[14:],
                        'Visa Handle': device,
                        'Script Status': 'Inactive',
                        'Resource': dev
                    }})


            except Exception as e:

                print(str(e)  + ' {initDevice, detectDevices, line 85}')



    def startThread(self, function, arguments):

        self.threadx = threading.Thread(target=function, args=arguments)
        self.threadx.daemon = True
        self.threadx.start()

    def vidValidator(self):
        devices = []
        devices_VID_PID = []
        devNames = []
        devInfo = {}
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
                devNames.append(x.friendly_name)
                devInfo.update({h[1][8:12] + h[1][17:]: x.friendly_name})
            except AttributeError:
                devInfo.update({h[1][8:12] + h[1][17:]: str(x)})
                pass
        return devInfo

class device:

    def __init__(self, *args):

        self.deviceName = args[0]
        self.VID_PID = args[1]
        self.modelName = args[2]

        pass

    def open(self):
        initDevice.devices.update({"first": "Two"})
        pass




