from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_to_chromedriver = '//home/melbin/Documents/chromedriver' # change path as needed
driver = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://www.lexisnexis.com/hottopics/lnacademic/?verb=sf&amp;sfi=AC00NBGenSrch'
driver.get(url)

driver.switch_to.frame('mainFrame')
#driver.find_element_by_id('terms')
search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "terms")))
search.clear()
search.send_keys('balloon')
search.send_keys(Keys.RETURN)

