from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/index.php?route=common/home&language=en-gb")
        listA = driver.find_elements(By.TAG_NAME, 'a')
        print(len(listA))
        for i in listA:
            print(i.text)
        time.sleep(5)

findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()