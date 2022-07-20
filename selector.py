import os
from unicodedata import category 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://hamrobazaar.com/login')
driver.implicitly_wait(5)

sum1 = driver.find_element_by_class_name('PhoneInputInput')
sum2 = driver.find_element_by_name('password')

sum1.send_keys(9843789700)
sum2.send_keys('prabin@737')

cl = driver.find_elements_by_class_name('btn btn--form full')[0]
cl.click()

driver.implicitly_wait(5)

# categorgy of jobs

get_jobs = driver.get('https://hamrobazaar.com/category/jobs/010f9add-2a94-468d-a937-02bb42f50fa2')
