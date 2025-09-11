from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CommonMethods:
    def get_table_data(self, table: WebElement):
        table_data = []
        rows = table.find_elements(By.XPATH, ".//tbody/tr")
        for row in rows:
            cells = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            table_data.append(cells)
        return table_data