import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.title("Amazon Search Bar Test")
@allure.description("Test Amazon.in login and search for 'pen'")
def test_amazon_search():
    AMAZON_EMAIL = "umatepinak@gmail.com"
    AMAZON_PASSWORD = "27@Ryzen"

    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

    #Blocker page
    with allure.step("Sign in to Amazon"):
        sign_in = wait.until(EC.element_to_be_clickable((By.ID, "nav-link-accountList")))
        sign_in.click()
        email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ap_email_login']")))
        email_input.send_keys(AMAZON_EMAIL)
        driver.find_element(By.ID, "continue").click()
        password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ap_password']")))
        password_input.send_keys(AMAZON_PASSWORD)
        driver.find_element(By.ID, "signInSubmit").click()

    with allure.step("Search for 'pen'"):
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys("pen")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "pen" in driver.page_source.lower(), "'pen' not found in the webpage"

    driver.quit()