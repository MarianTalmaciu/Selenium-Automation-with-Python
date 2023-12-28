from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElementByLINKTEXT():
    def locate_by_link_text_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/index.php?route=common/home&language=en-gb")
        search_field = driver.find_element(By.LINK_TEXT, "Cameras")
        search_field.click()
        time.sleep(5)

findbyid = DemoFindElementByLINKTEXT()
findbyid.locate_by_link_text_demo()


