import pytest
from pages.devices.modbus_devices_page import ModbusDevices


class TestModbusDevices:
    @classmethod
    def setup_class(cls):
        cls.modbus_devices = ModbusDevices(cls.driver, timeout=20)
        cls.modbus_devices.click_to_enter_test_page()
        
    def test_add_device(self):
        self.modbus_devices.add_device()
        assert "AHB20250917" in self.modbus_devices.get_meter_table()
        
    def test_delete_meter(self):
        self.modbus_devices.delete_meter("AHB20250917")
    
        