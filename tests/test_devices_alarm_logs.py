import pytest
from pages.devices.alarm_logs_page import AlarmLogs


class TestAlarmLogs:
    @classmethod
    def setup_class(cls):
        cls.alarm_logs = AlarmLogs(cls.driver, timeout=10)
        cls.alarm_logs.click_tab_enter_test_page()
        
    def test_interval_select(self):
        lft_col_bf, lft_col_af, lft_mt_bf, lft_mt_af, rgt_col_bf, rgt_col_af, rgt_mt_bf, rgt_mt_af = self.alarm_logs.interval_select()
        self.alarm_logs.logger.info(f"{lft_col_bf}, {lft_col_af}, {lft_mt_bf}, {lft_mt_af}")
        self.alarm_logs.logger.info(f"{rgt_col_bf}, {rgt_col_af}, {rgt_mt_bf}, {rgt_mt_af}")
        
        