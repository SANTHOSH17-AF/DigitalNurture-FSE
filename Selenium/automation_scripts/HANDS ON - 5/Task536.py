"""
Step 36 - Bootstrap Alerts demo: click 'Success Message' button, wait for the
success alert to become visible using WebDriverWait + EC.visibility_of_element_located,
then assert the alert text contains 'successfully'.
"""

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

alert_el = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#SuccessMessageBs"))
)

assert "successfully" in alert_el.text.lower()
print("Alert text:", alert_el.text)

driver.quit()
