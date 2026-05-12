import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("SF_USERNAME"),
        "password": os.getenv("SF_PASSWORD"),
    }