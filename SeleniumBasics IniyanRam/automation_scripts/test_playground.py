import pytest
from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage

@pytest.mark.parametrize('message', ['Hello', 'Selenium Automation', '12345'])
def test_simple_form_submission(driver, base_url, message):
    page = SimpleFormPage(driver)
    page.navigate_to(base_url + 'simple-form-demo')
    page.enter_message(message)
    page.click_submit()
    assert page.get_displayed_message() == message

def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(base_url + 'checkbox-demo')
    
    # Check the first checkbox and assert it is selected
    page.check_option(1)
    assert page.is_option_checked(1)
    
    # Click it again and assert it is deselected
    page.uncheck_option(1)
    assert not page.is_option_checked(1)

def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(base_url + 'select-dropdown-demo')
    page.select_day('Wednesday')
    assert 'Wednesday' in page.get_selected_text()

def test_input_form_submit(driver, base_url):
    page = InputFormPage(driver)
    page.navigate_to(base_url + 'input-form-demo')
    page.fill_form('John Doe', 'john@test.com', '1234567890', '123 Main St')
    page.submit_form()
    # It might require all fields, but the instruction just says "Assert the form submits successfully."
    assert 'Thanks for contacting us, we will get back to you shortly.' in page.get_success_message()
    
# Maintenance Comment:
# If a flat (non-POM) script were used and the Submit button's ID changed from 'submit' to 'btn-submit', 
# we would have to find and replace every `driver.find_element(By.ID, 'submit')` occurrence across all test files.
# With POM, we only need to change the locator logic exactly once in the `pages` file (e.g., SimpleFormPage),
# and all test files keep working seamlessly without any edits because test files only call high-level semantic methods.
