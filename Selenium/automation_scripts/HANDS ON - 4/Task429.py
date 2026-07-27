"""
Step 29 - open a new browser tab via execute_script, list window_handles,
switch to the new tab, and print its title.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL)

driver.execute_script('window.open("https://www.google.com");')
print("Open handles:", driver.window_handles)

driver.switch_to.window(driver.window_handles[1])
print("Second tab title:", driver.title)

driver.quit()
