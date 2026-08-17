import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup Jenkins-safe headless options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Safely install and locate ChromeDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    
    # Initialize Chrome
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    
    yield driver  # Provide driver to the tests
    
    # Teardown
    driver.quit()

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "login-button").click()
    
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error.is_displayed()
