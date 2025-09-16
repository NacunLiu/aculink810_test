import pytest
from pages.devices.dashboard_page import DevicesDashboard


class TestDevicesDashboard:
    @classmethod
    def setup_class(cls):
        cls.dashboard = DevicesDashboard(cls.driver)
        
    def test_dashboard(self):
       devices = self.dashboard.offline_devices()
       self.dashboard.logger.info(devices)
       alarms = self.dashboard.alarms()
       self.dashboard.logger.info(f"alarms on dashboard page are {alarms}")