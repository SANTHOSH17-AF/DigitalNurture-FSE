"""
Step 27 - run in headless mode using ChromeOptions and verify the title is
still printed correctly without a visible browser window.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1280,800")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
driver.implicitly_wait(10)

driver.get(BASE_URL)
print("Headless page title:", driver.title)

driver.quit()
