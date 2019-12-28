from selenium import webdriver
driver = webdriver.Chrome()

# open the the google web page
driver.get ('http://google.com')
element = driver.find_element_by_name('q'  )
element.send_keys('test')

# simulate someone pressing the RETURN or enter key
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)






# the end
