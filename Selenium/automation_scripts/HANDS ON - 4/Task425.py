"""
Step 24 - Selenium architecture (comment block):

- WebDriver: a library + browser-specific driver executable (e.g. chromedriver)
  that translates Python calls (driver.get, find_element, click...) into
  browser commands via the W3C WebDriver protocol. It talks directly to the
  real browser, so what we automate is genuine browser behaviour.
- Selenium Grid: solves running tests across many browser/OS combinations in
  parallel on multiple machines instead of one browser on one machine
  sequentially. A "hub" distributes sessions to registered "nodes."
- Selenium IDE: a browser extension for recording user interactions and
  playing them back, and for generating boilerplate code from that recording -
  useful for quickly bootstrapping a script, though generated code usually
  needs cleanup (better locators, waits) before real use.

Step 25 - minimal script: open Chrome via webdriver-manager, navigate to the
Selenium Playground, print the title, close the browser.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(BASE_URL)
print("Page title:", driver.title)

driver.quit()
