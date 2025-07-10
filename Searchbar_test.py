from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;

import time;

AMAZON_EMAIL = "umatepinak@gmail.com"
AMAZON_PASSWORD = "27@Ryzen"

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/");      
driver.maximize_window()

wait = WebDriverWait(driver, 30)

# Click on 'Sign in' button
sign_in = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='nav-link-accountList']/a")))
sign_in.click()

# Enter email and continue
email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ap_email_login']")))
email_input.send_keys(AMAZON_EMAIL)
driver.find_element(By.ID, "continue").click()

# Enter password and sign in
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ap_password']" )))
password_input.send_keys(AMAZON_PASSWORD)
driver.find_element(By.XPATH, "//*[@id='signInSubmit']").click()

# Search for a product
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='twotabsearchtextbox']")))
search_box.send_keys("pen")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load and assert "pen" is present in the results
time.sleep(3)  # Give time for results to load
page_source = driver.page_source
assert "asdasda" in driver.page_source.lower(), "'pen' not found in the webpage"

driver.quit()