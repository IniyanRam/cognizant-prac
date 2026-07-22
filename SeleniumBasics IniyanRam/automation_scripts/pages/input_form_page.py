from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InputFormPage(BasePage):
    NAME = (By.ID, 'name')
    EMAIL = (By.ID, 'inputEmail4')
    PASSWORD = (By.ID, 'inputPassword4')
    COMPANY = (By.ID, 'company')
    WEBSITE = (By.ID, 'websitename')
    COUNTRY = (By.NAME, 'country')
    CITY = (By.ID, 'inputCity')
    ADDRESS1 = (By.ID, 'inputAddress1')
    ADDRESS2 = (By.ID, 'inputAddress2')
    STATE = (By.ID, 'inputState')
    ZIP = (By.ID, 'inputZip')
    SUBMIT = (By.XPATH, "//button[text()='Submit']")
    SUCCESS = (By.CLASS_NAME, 'success-msg')
    
    def fill_form(self, name, email, phone, address):
        self.wait_for_element(self.NAME).send_keys(name)
        self.wait_for_element(self.EMAIL).send_keys(email)
        self.wait_for_element(self.PASSWORD).send_keys("password123")
        self.wait_for_element(self.COMPANY).send_keys("my company")
        self.wait_for_element(self.WEBSITE).send_keys("mycompany.com")
        self.wait_for_element(self.CITY).send_keys("New York")
        self.wait_for_element(self.ADDRESS1).send_keys(address)
        self.wait_for_element(self.ADDRESS2).send_keys("Apt 4B")
        self.wait_for_element(self.STATE).send_keys("NY")
        self.wait_for_element(self.ZIP).send_keys("10001")
        Select(self.wait_for_element(self.COUNTRY)).select_by_visible_text("United States")
        
    def submit_form(self):
        self.wait_for_element(self.SUBMIT).click()
        
    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS).text
