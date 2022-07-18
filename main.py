import os
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

# os.environ['PATH'] += "C:\chromedriver"


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://wordpress.org/download/")
# my_element = driver.find_element("id", "download-the-app-windows-64")
driver.implicitly_wait(2)
my_element = driver.find_element_by_id('download-wordpress')
my_element.click()

my_second_element = driver.find_element_by_id()