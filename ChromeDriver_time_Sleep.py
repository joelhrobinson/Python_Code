import time
from selenium import webdriver
driver = webdriver.Chrome()

# open the the google web page
driver.get ('http://google.com')
element = driver.find_element_by_name('q'  )
### element.send_keys('test')
element.send_keys('joelhrobinson.com')
# element.send_keys('chromedriver tutorial')
# element.send_keys('webdriver tutorial')
time.sleep (3)
# simulate someone pressing the RETURN or enter key
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)
time.sleep (3)
############################################
## JOEL: you need to set up the path variable first.   
# copy chromedriver.exe to d:\bin,
# then change system variable to include c:\bin
##############################################################