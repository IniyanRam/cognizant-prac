"""
Selenium Components:
- WebDriver: An API and protocol that controls a web browser natively, acting as the bridge between your test code and the browser.
- Selenium Grid: A hub-and-node system that allows tests to be executed in parallel across multiple machines and browser combinations.
- Selenium IDE: A browser extension for record-and-playback of interactions, mostly used for prototyping or generating quick scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# 27. Run in headless mode
options = Options()
options.add_argument('--headless')

# 25. Minimal script setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 26. Implicit wait (Bad practice globally because it blindly waits for all elements and masks timing issues, whereas explicit waits target specific conditions).
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")
print(driver.title)

driver.quit()
