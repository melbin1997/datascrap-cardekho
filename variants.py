from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://www.cardekho.com/new-hatchback+cars")
cars_dict = {}
variants_dict = {}

cars = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cartitle']//a")))
for i in cars:
    cars_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

variants = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='variantsDiv']//div[@class='magna']//a")))
for i in variants:
    variants_dict[i.get_attribute("title").encode('UTF8')] = i.get_attribute("href").encode('UTF8')

print cars_dict
print variants_dict

driver.close()