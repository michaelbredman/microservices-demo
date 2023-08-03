from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("http://boutique.chaos.harness-demo.site/")
WebDriverWait(driver, 10).until(EC.title_contains("Online Boutique"))

print(driver.title)
driver.close()
