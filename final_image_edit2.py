from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import datetime

print datetime.datetime.now()


###############################################
#a={1:2}				# !!!!!!!!!!!!!!!!!!!!!!!! run this only once !!!!!!!!!!!!!!!!!!!!!!!!
###############################################
#pickle.dump(a,open("images_found.p","wb"))
b=pickle.load(open("id.p","rb"))
c=pickle.load(open("images_found.p","rb"))
l=len(b)
g1=1
lis=[]
driver = webdriver.Chrome()

for key in b:
	q=time.time()
	if b[key] in c.keys():
		print
		print "Already fetched the pictures of ",b[key]
		print
		print c[b[key]]
		print
		print "Time taken= ",time.time()-q," seconds"
		print "Completed= ",g1,"/",l
		print "Percentage completed= ",g1*100/float(l)
		g1+=1
		#time.sleep(5)

	else:
		try:
			print
			print "Fetching the pictures of ",b[key]
			user_input =b[key]
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

			print
			print img_links
			a=pickle.load(open("images_found.p","rb"))
			a[b[key]]=img_links
			
			#storing the obtained data to the file
			pickle.dump(a,open("images_found.p","wb"))
			print
			print "Time taken= ",time.time()-q," seconds"
			print "Completed= ",g1,"/",l
			print "Percentage completed= ",g1*100/float(l)
			g1+=1
		except:
			print
			print "Couldnot obtain the pictures of ",b[key]
			driver.close()
			lis.append(b[key])
			print
			print "Time taken= ",time.time()-q," seconds"
			print "Completed= ",g1,"/",l
			print "Percentage completed= ",g1*100/float(l)
			g1+=1
			driver = webdriver.Chrome()
			time.sleep(5)



print
if len(lis)!=0:
	print "Pictures of the following cars couldnot be obtained ",lis
print "Task completed"
print datetime.datetime.now()