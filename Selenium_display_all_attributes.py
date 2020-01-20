############# tag_name ###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
#############################
element = 'Sorry!!!'
driver.get('http://google.com')
mystring = 'main'
#element = driver.find_element_by_name(mystring  )

element = driver.find_elements_by_xpath('//*[@id]')

for ii in element:
    # id name as string 
    nn1 = ii.tag_name
    nn2 = ii.get_attribute('name')
    ddd = ii.get_attribute('id')
    ccc = ii.get_attribute('class')
    vvv = ii.get_attribute('value')
    bbb = ii.get_attribute('buttonname')
    xxx = ii.get_attribute('xpath')
    print ("tag: ", nn1, nn2, ccc, ddd, vvv, bbb ) 
    if ccc == 'button':
        print ("XPath = ", xxx ) 
print ("Joel: Done")
