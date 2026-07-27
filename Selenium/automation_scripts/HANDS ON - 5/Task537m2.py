"""
Step 38 - wait for an element to be clickable before clicking it using
EC.element_to_be_clickable(), and explain the difference from
visibility_of_element_located.

Step 39 - use FluentWait (WebDriverWait with a custom poll_frequency and
ignored_exceptions) to poll every 500ms for up to 10 seconds, ignoring
NoSuchElementException, applied to a dynamically-loaded table row.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# --- Step 38: element_to_be_clickable ---
driver.get(BASE_URL + "bootstrap-alert-messages-demo/")

clickable_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#button1"))
)
clickable_button.click()
print("Clicked the button once it was confirmed clickable.")

# Difference between visibility_of_element_located and element_to_be_clickable:
# visibility_of_element_located only confirms the element exists in the DOM
# and has a non-zero size (i.e. it's visible on screen) - it says nothing
# about whether it can actually be interacted with. element_to_be_clickable
# does everything visibility_of_element_located does, AND additionally
# confirms the element is enabled (not disabled) and not obscured by another
# element on top of it (e.g. a loading spinner or modal overlay) - so it's
# the safer condition to wait for immediately before a .click() call.

# --- Step 39: FluentWait (poll every 500ms, max 10s, ignore NoSuchElementException) ---
driver.get(BASE_URL + "table-sort-search-demo/")

fluent_wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException],
)

row = fluent_wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "table tbody tr"))
print("First dynamically-loaded row text:", row.text)

driver.quit()
