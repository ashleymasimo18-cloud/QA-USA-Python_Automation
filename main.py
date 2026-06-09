import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from_address() == data.ADDRESS_FROM
        assert routes_page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        assert routes_page.get_active_plan() == "Supportive"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_phone_number_field()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next_for_phone()
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.enter_phone_code(code)
        routes_page.click_confirm_phone()
        assert routes_page.get_phone_number_value() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_payment_picker()
        routes_page.click_add_card()
        routes_page.enter_card_number(data.CARD_NUMBER)
        routes_page.enter_card_code(data.CARD_CODE)
        routes_page.click_link_button()
        routes_page.close_payment_modal()
        assert routes_page.get_payment_method() == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_blanket_toggle()
        assert routes_page.get_blanket_state() == True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        for i in range(2):
            routes_page.click_ice_cream_plus()
        assert routes_page.get_ice_cream_count() == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_phone_number_field()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next_for_phone()
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.enter_phone_code(code)
        routes_page.click_confirm_phone()
        routes_page.enter_comment(data.MESSAGE_FOR_DRIVER)
        routes_page.click_order_button()
        assert routes_page.is_car_search_modal_displayed() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
