import pytest
from pages.devices.virtual_devices_page import VirtualDevices
from time import sleep



class TestVirtualDevices:
    @classmethod
    def setup_class(cls):
        cls.virtual_devices = VirtualDevices(cls.driver)
        cls.virtual_devices.click_to_enter_test_page()
        
        
    def test_get_virtual_devices_list(self):
        virtual_devices_list = self.virtual_devices.get_virtual_device_list()
        print(virtual_devices_list)
        assert ['virtual_0426', 'AccuenergyVirtualDevice.virtual_0426', ''] in virtual_devices_list, self.virtual_devices.logger.error("virtual devices list test failed")
        self.virtual_devices.logger.info("virtual devices list test passed")
        
    def test_add_virtual_device(self):
        list = self.virtual_devices.add_virtual_device()
        print("virtual devices are")
        print(list)