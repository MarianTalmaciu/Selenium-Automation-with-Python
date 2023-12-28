from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        search_field = driver.find_element(By.ID, 'input-email')
        search_field.send_keys('testing@testing.com')
        # search_field.submit()
        time.sleep(5)

findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()