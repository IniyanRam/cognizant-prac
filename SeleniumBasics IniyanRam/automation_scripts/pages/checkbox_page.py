from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxPage(BasePage):
    def get_checkbox(self, index):
        return (By.XPATH, f"(//input[@type='checkbox'])[{index}]")
        
    def check_option(self, index):
        checkbox = self.wait_for_element(self.get_checkbox(index))
        if not checkbox.is_selected():
            checkbox.click()
            
    def uncheck_option(self, index):
        checkbox = self.wait_for_element(self.get_checkbox(index))
        if checkbox.is_selected():
            checkbox.click()
            
    def is_option_checked(self, index):
        return self.wait_for_element(self.get_checkbox(index)).is_selected()
