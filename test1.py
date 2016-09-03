import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CardekhoSearch(unittest.TestCase):

    def setUp(self):
        #user_input = raw_input("Enter : ")
        self.driver = webdriver.Firefox()

    def test_search_cardekho(self):
        user_input = "Maruti 800"
        driver = self.driver
        driver.get("https://www.cardekho.com/")
        #self.assertIn("CarDekho", driver.title)
        car_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
        car_name.clear()
        car_name.send_keys(user_input)
        car_name.send_keys(Keys.RETURN)
        #TODO : Change RETURN to search button click
        assert "No results found." not in driver.page_source
        driver.switch_to.default_content()
        #driver.findElement(By.linkText(user_input)).click()
        #driver.find_element_by_partial_link_text(user_input).click()
        found = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
        driver.find_element_by_css_selector("a[title*='" + user_input + "']").click()
        driver.find_element_by_css_selector("a[title*='Specs']").click()


        keyf_collection = driver.find_elements_by_xpath("//table[@class='keyfeature']/tbody/tr")

        #TODO : Change the method of printing
        print keyf_collection.len()
        for elem in keyf_collection:
            print elem.text




        '''techf_collection = driver.find_elements_by_xpath("//div[@class='specinner']/div/table")
        #cap = driver.find_elements_by_xpath("//div[@class='specinner']/div/table[1]/tbody")

        for elem in techf_collection:
            print elem.text'''

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()