from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import datetime

print datetime.datetime.now()
print 
p=time.time()
q = time.time()
driver = webdriver.Chrome()
driver.get("https://www.cardekho.com/")
driver.find_element_by_id("searchNewCarByBrandInputDiv").click()
s = driver.find_element_by_id("newCarBrandSelect")
a = [s.text]
a = [a[0].encode('UTF8') for x in a]
a = a[0].split('\n')
a = a[14:]
c = []
for i in range(15, 57):
    element = driver.find_element_by_xpath("//*[@id='newCarBrandSelect']/option[" + str(i) + "]").click()
    t = driver.find_element_by_id("newCarModelSelect")
    b=[]
    b = [t.text]
    b = [b[0].encode('UTF8') for x in b]
    b = b[0].split('\n')
    j=0
    while j<len(b):
        #print"helloo"
        if b[j]=='-Upcoming Model-' or b[j]=='-Upcoming Models-':
            b=b[0:j]
            #print"hiii"
        j+=1
    if '-Select Model-' in b:
        b.remove('-Select Model-')
    #print b
    #print i
    c.append(b)
    #print len(c[i-15])
    #time.sleep(1)
# print c
d = []
# print a
# print c

i = 0
while i < len(a):
    j = 0
    if len(c[i])==0:
        i+=1
        continue
    while j < len(c[i]):
        d.append(a[i] + ' ' + c[i][j])
        j += 1
    i += 1
print d     #list of all cars
driver.close()
print
print "Total No of cars=", len(d)
print "Total time taken=", time.time() - q, "seconds"
g13=len(d)

g12=1
for g10 in d:
    q=time.time()
    user_input = g10
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
    g11=pickle.load(open("output.p","rb"))
    g11[user_input]=car
    pickle.dump(g11,open("output.p","wb"))


    ############################################################################################################################


    # print category
    print
    print car
    print
    print "Time taken= ",time.time()-q," seconds"
    print "Data accured= ",g12,"/",g13
    print "Percentage completed= ",g12*100/float(g13)
    g12+=1
    # print
    # print "Time taken = ",time.time()-q," seconds"

    driver.close()
print
print "Task completed"
print datetime.datetime.now()