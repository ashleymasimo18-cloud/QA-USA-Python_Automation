from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:

    # Test 1 - Address
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    # Test 2 - Plan selection
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(@class,'button round')]")
    SUPPORTIVE_PLAN = (By.XPATH, "//div[@class='tcard-title' and text()='Supportive']")
    SUPPORTIVE_PLAN_PARENT = (By.XPATH, "//div[@class='tcard-title' and text()='Supportive']/..")
    ACTIVE_PLAN_TITLE = (By.XPATH, "//div[@class='tcard active']//div[@class='tcard-title']")

    # Test 3 - Phone number
    PHONE_NUMBER_FIELD = (By.CLASS_NAME, "np-button")
    PHONE_INPUT = (By.ID, "phone")
    PHONE_NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    PHONE_CODE_INPUT = (By.ID, "code")
    PHONE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    PHONE_NUMBER_VALUE = (By.CLASS_NAME, "np-text")

    # Test 4 - Credit card
    PAYMENT_PICKER = (By.CLASS_NAME, "pp-button")
    ADD_CARD = (By.XPATH, "//div[text()='Add card']")
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@id='number']")
    CARD_CODE_INPUT = (By.XPATH, "//input[@id='code' and @class='card-input']")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    PAYMENT_MODAL_CLOSE = (By.XPATH, "//div[contains(@class,'payment-picker open')]//button[@class='close-button section-close']")
    PAYMENT_METHOD_VALUE = (By.XPATH, "//div[@class='pp-value-text']")

    # Test 5 - Driver comment
    COMMENT_FIELD = (By.ID, "comment")

    # Test 6 - Blanket and handkerchiefs
    BLANKET_SLIDER = (By.XPATH, "//div[@class='r-sw']//span[@class='slider round']")
    BLANKET_CHECKBOX = (By.XPATH, "//div[@class='r-sw']//input[@type='checkbox']")

    # Test 7 - Ice cream
    ICE_CREAM_PLUS = (By.XPATH, "//div[@class='counter-plus']")
    ICE_CREAM_COUNT = (By.XPATH, "//div[@class='counter-value']")

    # Test 8 - Order taxi
    ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
    CAR_SEARCH_MODAL = (By.XPATH, "//div[@class='order-body']")

    def __init__(self, driver):
        self.driver = driver

    # Test 1 methods
    def enter_address(self, from_value, to_value):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_value)
        self.driver.find_element(*self.TO_FIELD).send_keys(to_value)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def get_to_address(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    # Test 2 methods
    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)).click()

    def select_supportive_plan(self):
        parent = self.driver.find_element(*self.SUPPORTIVE_PLAN_PARENT)
        if "active" not in parent.get_attribute("class"):
            self.driver.find_element(*self.SUPPORTIVE_PLAN).click()

    def get_active_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_TITLE).text

    # Test 3 methods
    def click_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).click()

    def enter_phone_number(self, phone):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PHONE_INPUT))
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def click_next_for_phone(self):
        self.driver.find_element(*self.PHONE_NEXT_BUTTON).click()

    def enter_phone_code(self, code):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PHONE_CODE_INPUT))
        self.driver.find_element(*self.PHONE_CODE_INPUT).send_keys(code)

    def click_confirm_phone(self):
        self.driver.find_element(*self.PHONE_CONFIRM_BUTTON).click()

    def get_phone_number_value(self):
        return self.driver.find_element(*self.PHONE_NUMBER_VALUE).text

    # Test 4 methods
    def click_payment_picker(self):
        self.driver.find_element(*self.PAYMENT_PICKER).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ADD_CARD)).click()

    def enter_card_number(self, number):
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(number)

    def enter_card_code(self, code):
        field = self.driver.find_element(*self.CARD_CODE_INPUT)
        field.send_keys(code)
        field.send_keys(Keys.TAB)

    def click_link_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.LINK_BUTTON)).click()

    def close_payment_modal(self):
        self.driver.find_element(*self.PAYMENT_MODAL_CLOSE).click()

    def get_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_VALUE).text

    # Test 5 methods
    def enter_comment(self, message):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(message)

    def get_comment(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_attribute("value")

    # Test 6 methods
    def click_blanket_toggle(self):
        self.driver.find_element(*self.BLANKET_SLIDER).click()

    def get_blanket_state(self):
        return self.driver.find_element(*self.BLANKET_CHECKBOX).get_property("checked")

    # Test 7 methods
    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNT).text

    # Test 8 methods
    def click_order_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

    def is_car_search_modal_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CAR_SEARCH_MODAL)).is_displayed()
