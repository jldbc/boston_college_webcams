from urllib2 import urlopen
from selenium import webdriver
import time
import random
import requests

driver = webdriver.Chrome('path/to/chromedriver')
driver.get("http://bolanee.bc.edu:8080/home.html?src=1&mode=0")

while True:
	img = driver.find_element_by_xpath('//html/body[@id="webcamXP-body"]/div[@id="container"]/div[@id="intro"]/div[@class="wxpcontainer"]\
		/div[@id="wxpcamdiv"]/img')
	# get the image source
	src = img.get_attribute("src")
	r = requests.get(src)
	with open('cam_photo.jpg','wb') as f:
		f.write(r.content)
	sleeptime = random.randint(3,15)
	time.sleep(sleeptime)
	#print 'tick'
	
driver.close()
