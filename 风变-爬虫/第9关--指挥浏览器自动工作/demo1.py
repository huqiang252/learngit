# -*- coding: utf-8 -*-
from selenium import webdriver
import time


url='https://localprod.pandateacher.com/python-manuscript/hello-spiderman/'


driver=webdriver.Chrome()
value=driver.get(url)
print(value)
print(type(value))
time.sleep(2)

teacher=driver.find_element_by_name('teacher')
teacher.send_keys('胡强')

assistant=driver.find_element_by_id('assistant')
assistant.send_keys('谢育花')
time.sleep(1)
subButton=driver.find_element_by_class_name('sub')
subButton.click()
time.sleep(1)
driver.close()