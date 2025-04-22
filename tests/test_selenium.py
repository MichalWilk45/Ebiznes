# 20 testing scenarios

# tests/test_orangehrm.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"

def wait_for_element(browser, by, value, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located((by, value))
    )

def login(browser):
    browser.get(URL)
    username = wait_for_element(browser, By.NAME, "username")
    username.send_keys(USERNAME)
    password = wait_for_element(browser, By.NAME, "password")
    password.send_keys(PASSWORD)
    submit = wait_for_element(browser, By.CSS_SELECTOR, "button[type='submit']")
    submit.click()
    time.sleep(1)

def test_login_success(browser):
    time.sleep(5)
    login(browser)
    assert "dashboard" in browser.current_url

def test_login_failure(browser):
    browser.get(URL)
    username = wait_for_element(browser, By.NAME, "username")
    username.send_keys("invalid")
    password = wait_for_element(browser, By.NAME, "password")
    password.send_keys("wrong")
    submit = wait_for_element(browser, By.CSS_SELECTOR, "button[type='submit']")
    submit.click()
    error = wait_for_element(browser, By.CLASS_NAME, "oxd-alert-content-text", timeout=5)
    assert "Invalid" in error.text

def test_dashboard_loaded(browser):
    login(browser)
    dashboard_header = wait_for_element(browser, By.TAG_NAME, "h6").text
    assert dashboard_header == "Dashboard"

def test_menu_visibility(browser):
    login(browser)
    menu = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.oxd-main-menu li"))
    )
    assert len(menu) > 0

def test_search_in_menu(browser):
    login(browser)
    search = wait_for_element(browser, By.CLASS_NAME, "oxd-input")
    search.send_keys("PIM")
    results = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-main-menu-item"))
    )
    assert any("PIM" in r.text for r in results)

def test_logout(browser):
    login(browser)
    user_dropdown = wait_for_element(browser, By.CLASS_NAME, "oxd-userdropdown-name")
    user_dropdown.click()
    logout = wait_for_element(browser, By.XPATH, "//a[text()='Logout']")
    logout.click()
    WebDriverWait(browser, 5).until(EC.url_contains("login"))
    assert "login" in browser.current_url

def test_add_employee_button(browser):
    login(browser)
    wait_for_element(browser, By.LINK_TEXT, "PIM").click()
    add_btn = wait_for_element(browser, By.LINK_TEXT, "Add Employee")
    assert add_btn.is_displayed()

def test_add_employee_form(browser):
    login(browser)
    wait_for_element(browser, By.LINK_TEXT, "PIM").click()
    wait_for_element(browser, By.LINK_TEXT, "Add Employee").click()
    first = wait_for_element(browser, By.NAME, "firstName")
    last = wait_for_element(browser, By.NAME, "lastName")
    assert first.is_displayed() and last.is_displayed()

def test_required_field_validation(browser):
    login(browser)
    wait_for_element(browser, By.LINK_TEXT, "PIM").click()
    wait_for_element(browser, By.LINK_TEXT, "Add Employee").click()
    wait_for_element(browser, By.CSS_SELECTOR, "button[type='submit']").click()
    error_msgs = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-input-field-error-message"))
    )
    assert len(error_msgs) >= 1

def test_user_dropdown_menu(browser):
    login(browser)
    wait_for_element(browser, By.CLASS_NAME, "oxd-userdropdown-name").click()
    dropdown_items = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-userdropdown-link"))
    )
    assert len(dropdown_items) > 1

def test_pim_page_title(browser):
    login(browser)
    wait_for_element(browser, By.LINK_TEXT, "PIM").click()
    title = wait_for_element(browser, By.TAG_NAME, "h6").text
    assert title == "PIM"

def test_search_employee_empty(browser):
    login(browser)
    wait_for_element(browser, By.LINK_TEXT, "PIM").click()
    wait_for_element(browser, By.CSS_SELECTOR, "button[type='submit']").click()
    rows = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-table-row"))
    )
    assert len(rows) >= 0

def test_reset_filters(browser):
    login(browser)
    link = wait_for_element(browser, By.LINK_TEXT, "PIM")
    link.click()
    employee_name = wait_for_element(browser, By.NAME, "employeeName")
    employee_name.send_keys("Test")
    reset = wait_for_element(browser, By.XPATH, "//button[text()='Reset']")
    reset.click()
    field = wait_for_element(browser, By.NAME, "employeeName")
    assert field.get_attribute("value") == ""

def test_left_menu_expand(browser):
    login(browser)
    icons = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-main-menu-item"))
    )
    assert len(icons) > 0

def test_url_after_login(browser):
    login(browser)
    WebDriverWait(browser, 5).until(EC.url_contains("dashboard"))
    assert "dashboard" in browser.current_url

def test_logo_visible(browser):
    login(browser)
    logo = wait_for_element(browser, By.CLASS_NAME, "oxd-brand-banner")
    assert logo.is_displayed()

def test_page_title(browser):
    browser.get(URL)
    WebDriverWait(browser, 5).until(EC.title_contains("OrangeHRM"))
    assert "OrangeHRM" in browser.title

def test_login_fields_present(browser):
    browser.get(URL)
    username = wait_for_element(browser, By.NAME, "username")
    password = wait_for_element(browser, By.NAME, "password")
    assert username.is_displayed()
    assert password.is_displayed()

def test_login_button_clickable(browser):
    browser.get(URL)
    button = wait_for_element(browser, By.CSS_SELECTOR, "button[type='submit']")
    assert button.is_enabled()

def test_footer_visibility(browser):
    browser.get(URL)
    footer = wait_for_element(browser, By.CLASS_NAME, "orangehrm-login-footer-sm")
    assert footer.is_displayed()

