from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

q = time.time()
user_input = "Bentley Bentayga"
driver = webdriver.Chrome()
driver.get("https://www.cardekho.com/")
car_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
car_name.clear()
car_name.send_keys(user_input)
car_name.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.switch_to.default_content()
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "a[title*='" + user_input + "']"))).click()
driver.find_element_by_css_selector("a[title*='" + user_input + "']").click()

driver.find_element_by_css_selector("a[href*='specification']").click()


############################################################################################################################


category = {}
keyf_collection = driver.find_elements_by_xpath("//table[@class='keyfeature']/tbody/tr")
key_specs = {}

# Displays key features
for elem in range(len(keyf_collection)):
    td = keyf_collection[elem].find_elements_by_tag_name('td')
    for index, i in enumerate(td):
        # Even numbers are the keys and Odd numbers are the values
        if index % 2 == 1:
            key_specs[td[index - 1].text.encode('UTF8')] = i.text.encode('UTF8')
category.setdefault('Key Specs', []).append(key_specs)


############################################################################################################################



techf_collection = driver.find_elements_by_xpath("//div[@class='specinner']/div/table")

# Displays technical specs
for li in range(len(techf_collection)):
    catg = techf_collection[li].find_elements_by_xpath("//div[@class='specinner']/div/table//th")[li].get_attribute(
        'title').encode('UTF8')
    tr = techf_collection[li].find_elements_by_tag_name('tr')
    specs = {}
    for i in range(len(tr)):
        td = tr[i].find_elements_by_tag_name('td')
        for index, j in enumerate(td):
            # Even numbers are the keys and Odd numbers are the values
            if index % 2 == 1:
                if 'has not' in j.get_attribute('title'):
                    specs[td[index - 1].text.encode('UTF8')] = 'False'
                elif 'has' in j.get_attribute('title'):
                    specs[td[index - 1].text.encode('UTF8')] = 'True'
                else:
                    specs[td[index - 1].text.encode('UTF8')] = j.text.encode('UTF8')
    category.setdefault(catg, []).append(specs)
car = {user_input: category}


############################################################################################################################


# print category
print car

# print
# print "Time taken = ",time.time()-q," seconds"

driver.close()
