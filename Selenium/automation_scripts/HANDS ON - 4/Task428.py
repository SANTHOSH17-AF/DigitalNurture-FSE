"""
Step 28 - open the Selenium Playground, navigate to Simple Form Demo (click
the link), assert the URL contains 'simple-form-demo', then navigate back.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL)

simple_form_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
simple_form_link.click()

assert "simple-form-demo" in driver.current_url
print("Navigated to:", driver.current_url)

driver.back()
print("Back on:", driver.current_url)

driver.quit()
