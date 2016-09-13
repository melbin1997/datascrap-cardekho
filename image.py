from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

q=time.time()
user_input = "Maruti 800"
driver = webdriver.Chrome()
driver.get("https://www.cardekho.com/")
car_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
car_name.clear()
car_name.send_keys(user_input)
car_name.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.switch_to.default_content()


#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "a[title*='" + user_input + "']"))).click()
driver.find_element_by_css_selector("a[title*='" + user_input + "']").click()
driver.find_element_by_css_selector("a[href*='pictures']").click()
driver.find_element_by_xpath("//div[@class='overlay']").click()
images = driver.find_elements_by_xpath("//div[@class='owl-item loading']//img")


#Storing link of images
img_links = []
for i,img in enumerate(images):
	if img.get_attribute('data-src')!=None:
		img_links.append(img.get_attribute('data-src').encode('UTF8'))


print img_links
driver.close()
print
print "Time taken= ",time.time()-q," seconds"