from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        search_field = driver.find_element(By.TAG_NAME, 'input')
        # search_field = driver.find_element(By.CLASS_NAME, "form-control")
        search_field.send_keys('testing@testing.com')
        # driver.implicitly_wait(5)
        time.sleep(5)


findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()