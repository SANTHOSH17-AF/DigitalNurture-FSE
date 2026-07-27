"""
Step 31 - demonstrate get_window_size() and set_window_size(1280, 800), and
explain why a consistent window size matters for responsive UI automation.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get(BASE_URL)

print("Current size:", driver.get_window_size())
driver.set_window_size(1280, 800)
print("New size:", driver.get_window_size())

# Why consistent window size matters for responsive UI automation:
# Many modern web apps use responsive breakpoints that hide, collapse, or
# rearrange elements at different viewport widths (e.g. a nav menu collapses
# into a hamburger icon below 768px). If tests run with an unpredictable or
# default window size, a locator that works at one size might not exist, or
# might be covered by another element, at a different size - causing flaky,
# environment-dependent failures. Pinning a consistent size makes runs
# reproducible across machines, CI pipelines, and team members.

driver.quit()
