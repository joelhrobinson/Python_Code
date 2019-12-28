############################################
## JOEL: you need to set up the path variable first.  It cannot find the files 
# copy chromedriver.exe to d:\bin, then change system variable to include c:\bin
# the end
#############################################
import time
from selenium import webdriver
driver = webdriver.Chrome()

# open the the google web page
driver.get ('http://google.com')
element = driver.find_element_by_name('q'  )
element.send_keys('Python Tutorials')

# simulate someone pressing the RETURN or enter key
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)
time.sleep (5)
print ('done')
