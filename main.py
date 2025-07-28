import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://prod.myfbo.com/link.asp?fbo=aoal")

time.sleep(10)

driver.quit()