import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

def test_login_salesforce(driver):
    driver.get("https://login.salesforce.com")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(os.getenv("SF_USERNAME"))
    driver.find_element(By.ID, "password").send_keys(os.getenv("SF_PASSWORD"))
    driver.find_element(By.ID, "Login").click()
    wait.until(EC.url_contains("force.com"))
    assert "force.com" in driver.current_url