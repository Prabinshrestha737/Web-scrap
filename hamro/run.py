from hamro import Booking


with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency='GBP')
    bot.select_place_to_go("New York")
    bot.select_dates(check_in_date='2022-07-24',
    check_out_date='2022-07-26')

    bot.select_number_of_peoples(10)
    bot.click_search()
    bot.apply_filtrations()





