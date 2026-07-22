from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1280,800')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 28. Navigate to Simple Form Demo, assert URL, go back
driver.get("https://www.lambdatest.com/selenium-playground/")
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
assert 'simple-form-demo' in driver.current_url
driver.back()

# 29. Open new tab, switch, print Google title
driver.execute_script('window.open("https://www.google.com");')
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])
print(driver.title)

# 30. Switch back, take screenshot
driver.switch_to.window(window_handles[0])
driver.save_screenshot('playground_screenshot.png')

# 31. Window Size (Consistent window size matters for responsive UI automation to ensure elements are visibly rendered in expected locations rather than hidden by mobile menus).
print(driver.get_window_size())
driver.set_window_size(1280, 800)

driver.quit()
