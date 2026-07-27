"""
Step 34 - Checkbox Demo: use XPath with text() to find the first checkbox
label, and contains() to find all option labels.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL + "checkbox-demo/")

first_option = driver.find_element(By.XPATH, "//label[text()='Option 1']")
all_options = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")

print("First option:", first_option.text)
print("All options found:", len(all_options))

driver.quit()
