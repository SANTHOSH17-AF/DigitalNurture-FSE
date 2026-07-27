"""
Step 26 - add implicit wait and explain why a global implicit wait is
considered bad practice compared to explicit waits.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Why a global implicit wait is bad practice compared to explicit waits:
# implicitly_wait() applies the SAME fixed timeout to every find_element call
# for the entire driver session, regardless of what that specific element
# needs. It can only wait for an element to exist in the DOM - it can't wait
# for a specific condition like "visible AND clickable" or "text equals X".
# Mixing it with explicit WebDriverWait calls (Hands-On 5) can also create
# unpredictable, compounding wait times that are hard to debug. Explicit
# waits let each step wait for exactly the condition it needs, no more.

driver.get(BASE_URL)
print("Page title:", driver.title)

driver.quit()
