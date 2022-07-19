import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# os.environ['PATH'] += "C:\chromedriver"


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://wordpress.org/download/")
# my_element = driver.find_element("id", "download-the-app-windows-64")
driver.implicitly_wait(2)
my_element = driver.find_element_by_id('download-wordpress')
my_element.click()

# my_second_element = driver.find_element_by_id('sadasd')


WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'apps-mobile')# Element Filteration
        # The expected text

    )
)