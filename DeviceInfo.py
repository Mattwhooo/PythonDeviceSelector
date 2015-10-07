import xml.etree.ElementTree as ET
from lxml import html
import requests

class DeviceInfo:
    def __init__(self):
        tree = ET.parse("Devices.xml")
        self.root = tree.getroot()

    def getDevice(self, udid):
        deviceNode = self.root.findall(".//device[udid='" + udid + "']")
        try:
            device = {}
            device['udid'] = deviceNode[0].find('udid').text
            device['name'] = deviceNode[0].find('deviceName').text
            device['manufacturer'] = deviceNode[0].find('manufacturer').text
            device['model'] = deviceNode[0].find('model').text
            device['osv'] = deviceNode[0].find('osv').text
        except:
            pass
        return device

    def gridDevices(self):
        page = requests.get('http://10.238.242.218:4444/grid/console')
        tree = html.fromstring(page.text)
        return tree.xpath('//a[contains(@title, "ANDROID")]/text()')
