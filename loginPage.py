from PytestDemo.locators.locators import Locators
class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.username_text_id = Locators.username_text_id
        self.password_text_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalidUsername_message_xpath = "//span[contains(text(),'Invalid credentials')]"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_text_id).clear()
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_username_massage(self):
        msg =  self.driver.find_element_by_xpath(self.invalidUsername_message_xpath).text
        return msg
