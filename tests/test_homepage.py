from pageobjects.Homepage import Mainpage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_login(self):
        homepage = Mainpage(self.driver)
        logger = self.getLogger()
        actions = self.get_actions()

        self.validate_page_has_appeared(homepage.get_login_button_home_page())
        self.click_to_close(homepage.get_alert_advisory_close_button())

        loginpage = homepage.click_login_button()
        self.validate_page_has_appeared(loginpage.get_login_page_header())

        loginpage.login_to_delta("shihabSylhetTestOne", "Sylhettest", "$shihabSylhetTest1")
        homepage.validate_username_of_homepage_logged_in("Shihabtest")
        print("Test passed")

    def test_search_for_flight(self):
        homepage = Mainpage(self.driver)
        logger = self.getLogger()
        actions = self.get_actions()

        homepage.enter_cities_to_travel_to("DFW", "CMB")
        logger.info("Selecting type of trip")
        homepage.select_type_of_trip("One Way")
        homepage.date_picker(4, 5, 2023)
        homepage.pax_count_picker(5)
        homepage.hover_over_and_click_search_for_flights_button()






