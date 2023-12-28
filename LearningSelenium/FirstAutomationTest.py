from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

# driver = webdriver.Chrome(ChromeDriverManager().install())

# service = Service(executable_path='D:\PythonProjects\Python - Selenium\PythonSeleniumProject\chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demo.opencart.com/")
driver.maximize_window()
print(driver.title)
# driver.close()