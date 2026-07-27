"""
Step 37 - demonstrate why time.sleep(3) is bad: time the same wait done with
time.sleep(3) vs done with an explicit WebDriverWait, and compare.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL + "bootstrap-alert-messages-demo/")
driver.find_element(By.CSS_SELECTOR, "#button1").click()

# Version A: hard-coded sleep
start = time.time()
time.sleep(3)
alert_el_sleep = driver.find_element(By.CSS_SELECTOR, "#SuccessMessageBs")
print("Sleep approach took:", time.time() - start, "seconds")

driver.get(BASE_URL + "bootstrap-alert-messages-demo/")
driver.find_element(By.CSS_SELECTOR, "#button1").click()

# Version B: explicit wait
start = time.time()
alert_el_wait = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#SuccessMessageBs"))
)
print("Explicit wait approach took:", time.time() - start, "seconds")

# Comment on the difference: the sleep() version always burns the full 3
# seconds no matter what, even though the element is usually ready sooner.
# The explicit wait version returns as soon as the condition is actually
# satisfied - typically a fraction of a second here - so it's faster on a
# fast/healthy machine. On a slow machine or slow network, a fixed sleep(3)
# might not even be long enough and the test would fail, while WebDriverWait
# keeps polling up to its 10-second timeout and only fails if the element
# genuinely never appears - so it's both faster in the common case and more
# reliable in the slow case.

driver.quit()
