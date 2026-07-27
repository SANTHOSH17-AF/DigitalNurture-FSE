"""
Step 32 - locate the Simple Form Demo message input using all 6 locator
strategies: By.ID, By.NAME, By.CLASS_NAME, By.TAG_NAME, absolute XPath,
relative XPath.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL + "simple-form-demo/")

by_id = driver.find_element(By.ID, "user-message")
by_name = driver.find_element(By.NAME, "message")
by_class = driver.find_element(By.CLASS_NAME, "form-control")
by_tag = driver.find_element(By.TAG_NAME, "input")
by_xpath_absolute = driver.find_element(
    By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/form/div[1]/input"
)
by_xpath_relative = driver.find_element(By.XPATH, "//input[@id='user-message']")

print("Found via ID:", by_id.tag_name)
print("Found via NAME:", by_name.tag_name)
print("Found via CLASS_NAME:", by_class.tag_name)
print("Found via TAG_NAME:", by_tag.tag_name)
print("Found via absolute XPath:", by_xpath_absolute.tag_name)
print("Found via relative XPath:", by_xpath_relative.tag_name)

driver.quit()
