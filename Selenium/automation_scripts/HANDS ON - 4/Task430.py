"""
Step 30 - switch back to the original tab and take a screenshot, verifying
the file is created.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL)

driver.execute_script('window.open("https://www.google.com");')
driver.switch_to.window(driver.window_handles[1])

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])

screenshot_path = "playground_screenshot.png"
driver.save_screenshot(screenshot_path)

assert os.path.exists(screenshot_path)
print("Screenshot saved and verified at:", os.path.abspath(screenshot_path))

driver.quit()
