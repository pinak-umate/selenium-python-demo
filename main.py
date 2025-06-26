from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "python" in driver.title
elem = driver.find_element(By=By.NAME, value="q")
elem.clear()
elem.send_keys("python")
elem.send_keys(keys)
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()