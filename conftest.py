import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_for_element(browser):
    # Czekaj, aż element stanie się widoczny (np. przycisk lub inny element)
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'element_id'))
    )

    # Gdy element jest widoczny, możemy wykonać kliknięcie
    element.click()

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

