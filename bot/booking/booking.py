from select import select
from selenium import webdriver
import os 
import booking.constants as const 


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type,exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    
    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )

        currency_element.click()

        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )

        selected_currency_element.click()


    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )

        first_result.click()

    
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )

        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )

        check_out_element.click()

    
    def select_number_of_peoples(self, count=1):

        
        search_number_of_people = self.find_element_by_class_name('xp__guests__count')
        search_number_of_people.click()

        while True:
            decrease_people = self.find_element_by_css_selector(
                'button[data-bui-ref="input-stepper-subtract-button"]'
            )
            # decrease_people.click()

            #If the value of adults reaches 1, then we should get out
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            ) #Should give back the adults count

            if int(adults_value) == 1:
                break


            increase_button_element = self.find_element_by_css_selector(
                'button[data-bui-ref="input-stepper-add-button"]'
            )

            for _ in range(count - 1):
                increase_button_element.click()


    


    



    