import pytest
from pages.devices.alarm_logs_page import AlarmLogs


class TestAlarmLogs:
    @classmethod
    def setup_class(cls):
        cls.alarm_logs = AlarmLogs(cls.driver, timeout=10)
        cls.alarm_logs.click_tab_enter_test_page()
        
    def test_interval_select_date(self):
        lft_col_bf, lft_col_af, lft_mt_bf, lft_mt_af, rgt_col_bf, rgt_col_af, rgt_mt_bf, rgt_mt_af = self.alarm_logs.interval_select_date()
        self.alarm_logs.logger.info(f"{lft_col_bf}, {lft_col_af}, {lft_mt_bf}, {lft_mt_af}")
        self.alarm_logs.logger.info(f"{rgt_col_bf}, {rgt_col_af}, {rgt_mt_bf}, {rgt_mt_af}")
        
        
    def test_interval_select_time(self):
        reference = self.alarm_logs.common_methods.load_yaml_test_data("./reference/devices_alarm_logs.yml")
        hours, minutes, ampm = self.alarm_logs.interval_select_time()
        assert hours == reference["expected"]["hours"]
        assert minutes == reference["expected"]["minutes"]
        assert ampm == reference["expected"]["am_pm"]
        self.alarm_logs.logger.info(f"calendar hour options are{hours} \n  minutes options are{minutes} \n sections are{ampm}")
        
    def test_interval_select_clear_apply_button(self):
        interval_value = self.alarm_logs.interval_select_clear_apply_button()
        self.alarm_logs.logger.info(f"{interval_value}")
        assert "2025" in interval_value
        
    def test_interval_select_search(self):
        self.alarm_logs.interval_select_search()
        
    def test_alarm_log_table(self):
        alarm_data = self.alarm_logs.alarm_log_table()
        self.alarm_logs.logger.info(f"{alarm_data}")
    