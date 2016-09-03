import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CardekhoSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_cardekho(self):
        user_input = "Volkswagen Ameo"
        driver = self.driver
        driver.get("https://www.cardekho.com/")
        car_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cardekhosearchtext")))
        car_name.clear()
        car_name.send_keys(user_input)
        car_name.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.switch_to.default_content()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title*='" + user_input + "']")))
        driver.find_element_by_css_selector("a[title*='" + user_input + "']").click()



        '''driver = self.driver
        driver.get("https://www.cardekho.com/carmodels/Maruti/Maruti_800")'''

        driver.find_element_by_css_selector("a[title*='Specs']").click()
        keyf_collection = driver.find_elements_by_xpath("//table[@class='keyfeature']/tbody/tr")
        #Displays key features
        for elem in range(len(keyf_collection)):
            td = keyf_collection[elem].find_elements_by_tag_name('td')
            for i in td:
                if(i.get_attribute('class') == 'lefttd' or i.get_attribute('class') == 'righttd'):
                    print i.text,
            print

        techf_collection = driver.find_elements_by_xpath("//div[@class='specinner']/div/table")
        #Displays technical specs
        for li in range(len(techf_collection)):
            print techf_collection[li].find_elements_by_xpath("//div[@class='specinner']/div/table//th")[li].get_attribute('title')
            tr = techf_collection[li].find_elements_by_tag_name('tr')
            for i in range(len(tr)):
                td = tr[i].find_elements_by_tag_name('td')
                for j in td:
                    print j.text,
                    if('has not' in j.get_attribute('title')):
                        print "False",
                    elif('has' in j.get_attribute('title')):
                        print "True",
                print
            print

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()