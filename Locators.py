from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

#CSS Selector
driver.find_element(By.NAME, "q").send_keys("abc")