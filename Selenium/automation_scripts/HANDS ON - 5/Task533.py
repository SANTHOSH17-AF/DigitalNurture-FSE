"""
Step 33 - locate the same message input using By.CSS_SELECTOR, written 3
different ways: by ID, by attribute, by parent-child relationship.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL + "simple-form-demo/")

css_by_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
css_by_attr = driver.find_element(By.CSS_SELECTOR, "[name='message']")
css_by_parent_child = driver.find_element(By.CSS_SELECTOR, "div > input#user-message")

print("Found via CSS (#id):", css_by_id.tag_name)
print("Found via CSS ([name=value]):", css_by_attr.tag_name)
print("Found via CSS (div > input):", css_by_parent_child.tag_name)

driver.quit()
