import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver

    # Teardown
    driver.quit()


# Step 48: session-scoped base_url fixture
@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


# Step 46: capture a screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            test_name = item.name.replace("/", "_").replace("::", "_")
            driver.save_screenshot(f"{test_name}_failure.png")
