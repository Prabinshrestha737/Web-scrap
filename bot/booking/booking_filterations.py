# This file includes a class with instance methods that will be responsible to interact with our website
# AFter we habe some results, to apply filtrations 

from selenium.webdriver.remote.webdriver import WebDriver

from typing import List 

class BookingFilterations:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    
    def apply_star_rating(self):    
        start_filteration_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_child_elements = self.driver.find_element_by_css_selector(
            '*'
        )

        d = self.driver.find_element_by_css_selector(
            'div[data-filters-item="class:class=1"]'
        )

        d.click()
