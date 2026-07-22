from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    SELECT_ELEM = (By.ID, 'select-demo')
    RESULT = (By.CLASS_NAME, 'selected-value')
    
    def select_day(self, day_name):
        select = Select(self.wait_for_element(self.SELECT_ELEM))
        select.select_by_visible_text(day_name)
        
    def get_selected_text(self):
        return self.wait_for_element(self.RESULT).text
