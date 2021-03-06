import calendar

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


from pageobjects.Loginpage import LoginPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class Mainpage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    alert_advisory_close_button = (By.XPATH, "//button[contains(@class, 'advisory-close-icon')]")
    alert_advisory_close_button_XPath = "//button[contains(@class, 'advisory-close-icon')]"

    login_button_home_page = (By.XPATH, "//button[contains(@class, 'login')]")
    login_button_home_page_XPath = "//button[contains(@class, 'login')]"

    overlay_image_advertisement = (By.XPATH, "//div[contains(@class, 'card-img-overlay')]")
    overlay_image_advertisement_XPath = "//div[contains(@class, 'card-img-overlay')]"

    home_page_logged_in_username_displayed = (By.XPATH, "//span[@class = 'pax-name']")
    home_page_logged_in_username_displayed_XPath = "//span[@class = 'pax-name']"

    type_of_trip_dropdown_selector = (By.XPATH, "//span[@id = 'selectTripType-val']")
    type_of_trip_dropdown_selector_XPath = "//span[@id = 'selectTripType-val']"

    origin_city = (By.XPATH, "//a[@id='fromAirportName']")
    origin_city_XPath = "//a[@id='fromAirportName']"

    arrival_city = (By.XPATH, "//a[@id='toAirportName']")
    arrival_city_XPath = "//a[@id='toAirportName']"

    first_dropdown_suggestion = (By.XPATH, "//a[@class='airportLookup-list']")
    first_dropdown_suggestion_XPath = "//a[@class='airportLookup-list']"

    city_search_box = (By.XPATH, "//input[@id='search_input']")
    city_search_box_XPath = "//input[@id='search_input']"

    date_picker_opener = (By.XPATH, "//div[@id='input_departureDate_1']")
    date_picker_opener_XPath = "//div[@id='input_departureDate_1']"

    date_picker_dep_after_select = (By.XPATH, "//span[@class = 'calenderDepartSpan']")
    date_picker_dep_after_select_XPath = "//span[@class = 'calenderDepartSpan']"

    select_next_month = (By.XPATH, "//a[@title='To select next month']")
    select_next_month_XPath = "//a[@title='To select next month']"

    done_button_date_picker = (By.XPATH, "//button[@value='done']")
    done_button_date_picker_XPath = "//button[@value='done']"

    pax_picker_dropdown_selector = (By.XPATH, "//span[@id='passengers-val']")
    pax_picker_dropdown_selector_XPath = "//span[@id='passengers-val']"

    pax_picker_dropdown_all_options_box = (By.XPATH, "//ul[@id = 'selectTripType-desc']")
    pax_picker_dropdown_all_options_box_XPath = "//ul[@id = 'selectTripType-desc']"

    search_for_all_flights_submit_button = (By.XPATH, "//button[@id='btn-book-submit']")
    search_for_all_flights_submit_button_XPath = "//button[@id='btn-book-submit']"

    type_of_trip_option_dynamic_xpath = "//ul[@id = 'selectTripType-desc']/li[contains(text(), '{}')]"
    date_picker_month_dynamic_xpath = "//span[contains(@class,'dl-datepicker-month') and contains(text(), '{}')]"
    date_picker_year_dynamic_xpath = "//span[contains(@class,'dl-datepicker-year') and contains(text(), '{}')]"
    number_of_pax_option_to_select_dynamic_xpath = "//ul[@id = 'passengers-desc']/li[contains(text(), '{}')]"

    @property
    def get_alert_advisory_close_button(self):
        return self.driver.find_element(*Mainpage.alert_advisory_close_button)

    @property
    def get_login_button_home_page(self):
        return self.driver.find_element(*Mainpage.login_button_home_page)

    @property
    def get_overlay_image_advertisement(self):
        return self.driver.find_element(*Mainpage.overlay_image_advertisement)

    @property
    def get_home_page_logged_in_username_displayed(self):
        return self.driver.find_element(*Mainpage.home_page_logged_in_username_displayed)

    @property
    def get_type_of_trip_dropdown_selector(self):
        return self.driver.find_element(*Mainpage.type_of_trip_dropdown_selector)

    @property
    def get_origin_city(self):
        return self.driver.find_element(*Mainpage.origin_city)

    @property
    def get_arrival_city(self):
        return self.driver.find_element(*Mainpage.arrival_city)

    @property
    def get_first_dropdown_suggestion(self):
        return self.driver.find_element(*Mainpage.first_dropdown_suggestion)

    @property
    def get_city_search_box(self):
        return self.driver.find_element(*Mainpage.city_search_box)

    @property
    def get_datepicker_opener(self):
        return self.driver.find_element(*Mainpage.date_picker_opener)

    @property
    def get_datepicker_dep_after_select(self):
        return self.driver.find_element(*Mainpage.date_picker_dep_after_select)

    @property
    def get_select_next_month(self):
        return self.driver.find_element(*Mainpage.select_next_month)

    @property
    def get_done_button_date_picker(self):
        return self.driver.find_element(*Mainpage.done_button_date_picker)

    @property
    def get_pax_picker_dropdown_selector(self):
        return self.driver.find_element(*Mainpage.pax_picker_dropdown_selector)

    @property
    def get_pax_picker_dropdown_all_options_box(self):
        return self.driver.find_element(*Mainpage.pax_picker_dropdown_all_options_box)

    @property
    def get_search_for_flights_submit_button(self):
        return self.driver.find_element(*Mainpage.search_for_all_flights_submit_button)

    def click_login_button(self):
        self.driver.find_element(*Mainpage.login_button_home_page).click()
        loginpage = LoginPage(self.driver)
        return loginpage

    def validate_username_of_homepage_logged_in(self, expectedFirstName):
        assert expectedFirstName == self.get_home_page_logged_in_username_displayed.text

    def enter_cities_to_travel_to(self, origin, arrival):
        self.click_to_close(self.get_alert_advisory_close_button)
        self.get_origin_city.click()
        actions = ActionChains(self.driver)
        actions.send_keys(origin)
        actions.perform()

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.first_dropdown_suggestion_XPath)))
        self.get_first_dropdown_suggestion.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.arrival_city_XPath)))
        self.get_arrival_city.click()
        a = ActionChains(self.driver)
        a.send_keys(arrival)
        a.perform()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.first_dropdown_suggestion_XPath)))
        self.get_first_dropdown_suggestion.click()

    def select_type_of_trip(self, triptype):
        assert self.get_type_of_trip_dropdown_selector.is_displayed()

        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_type_of_trip_dropdown_selector)
        actions.click()
        actions.perform()

        type_of_trip = self.driver.find_element(By.XPATH, self.type_of_trip_option_dynamic_xpath.format(triptype))
        type_of_trip.click()
        assert self.get_type_of_trip_dropdown_selector.text == triptype

    def date_picker(self, month_as_int, date_as_int, year_as_int):
        month_as_string = calendar.month_name[month_as_int]

        date_picker_month_header_xpath = self.date_picker_month_dynamic_xpath.format(month_as_string)
        date_picker_year_header_xpath = self.date_picker_year_dynamic_xpath.format(year_as_int)

        self.get_datepicker_opener.click()

        exception_handling = self.get_exception_handling()

        while not exception_handling.is_displayed_enhanced(date_picker_month_header_xpath, 1, self.driver) and not exception_handling.is_displayed_enhanced(date_picker_year_header_xpath, 1, self.driver):
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_select_next_month)
            actions.click()
            actions.perform()

        dates = "/ancestor::div[@class= 'dl-datepicker-header']/following-sibling::div[@class='dl-datepicker-calendar-cont']//a[text()= '{}']".format(date_as_int)
        date_picker_indiv_date_xpath = date_picker_month_header_xpath + dates
        date_picker_indiv_date = self.driver.find_element(By.XPATH, date_picker_indiv_date_xpath)

        a = ActionChains(self.driver)
        a.move_to_element(date_picker_indiv_date)
        a.click()
        a.move_to_element(self.get_done_button_date_picker)
        a.click()
        a.perform()

        assert f"{month_as_string[0:3]} {date_as_int}" == self.get_datepicker_dep_after_select.text

    def pax_count_picker(self, number_of_pax_one_to_nine):

        self.validate_page_has_appeared(self.get_pax_picker_dropdown_selector)

        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_pax_picker_dropdown_selector)
        actions.click()
        actions.perform()

        number_of_pax_option_to_select = self.driver.find_element(By.XPATH, self.number_of_pax_option_to_select_dynamic_xpath.format(number_of_pax_one_to_nine))
        print(number_of_pax_option_to_select)
        while "select-ui-optionList-hover" not in number_of_pax_option_to_select.get_attribute("class"):
            a = ActionChains(self.driver)
            a.send_keys(Keys.DOWN)
            a.perform()

        number_of_pax_option_to_select.click()

        assert f'{number_of_pax_one_to_nine} Passenger' in self.get_pax_picker_dropdown_selector.text

    def hover_over_and_click_search_for_flights_button(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_search_for_flights_submit_button)
        actions.click()
        actions.perform()





