from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

# 32 & 33. Locators
elem_id = driver.find_element(By.ID, "user-message")
# elem_name = driver.find_element(By.NAME, "...") # no actual name maybe, but just showcasing logic
elem_css1 = driver.find_element(By.CSS_SELECTOR, "#user-message")
elem_css2 = driver.find_element(By.CSS_SELECTOR, "[id='user-message']")
elem_css3 = driver.find_element(By.CSS_SELECTOR, "div > input#user-message")
elem_xpath_abs = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input")
elem_xpath_rel = driver.find_element(By.XPATH, "//input[@id='user-message']")

# 34. Checkbox demo logic
driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
elem_xpath_text = driver.find_element(By.XPATH, "//label[text()='Option 1']")
elems_xpath_contains = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")

'''
35. Locator Rankings (Most to Least Preferred):
1. ID (Fastest, unique)
2. NAME (Usually unique)
3. CSS Selector (Fast, readable, supports complex structures)
4. Class Name (Can be non-unique)
5. Relative XPath (Slower, but powerful for complex logic)
6. Absolute XPath (Very brittle, breaks if any HTML spacing changes)
'''

# 36. Explicit waits
driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
driver.find_element(By.XPATH, "//button[contains(text(), 'Autoclosable Success Message')]").click()

alert_elem = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success'))
)
assert 'successfully' in alert_elem.text.lower()

# 37. time.sleep vs explicit wait
# time.sleep(3) forces the script to block for exactly 3 seconds always, wasting time.
# WebDriverWait polls the DOM every 500ms and proceeds immediately when the condition is met, saving time and increasing reliability.

# 38. element_to_be_clickable
# visibility_of_element_located checks if element is in DOM and > 0px size.
# element_to_be_clickable checks if it is visible AND enabled (not disabled) so it can receive clicks.
wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.ID, "autoclosable-btn-success")))

# 39. FluentWait in Python (using WebDriverWait with custom poll frequency)
fluent_wait = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=[Exception])
fluent_wait.until(EC.visibility_of_element_located((By.ID, "autoclosable-btn-success")))

driver.quit()
