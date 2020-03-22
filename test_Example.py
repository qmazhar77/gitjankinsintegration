from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure
class TestHRM:
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            assert False
            self.driver.close()

    def test_listemployee(self):
        pytest.skip("Skipping test.. later I will implement")

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").submit()
        self.driver.find_element_by_link_text("Admin").click()
        #act_img = self.driver.find_element_by_xpath('//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[3]/div').is_displayed()
        #if act_img== True:
        #    print("Image Displayed")
        #else:

        act_title=self.driver.title

        if act_title=="OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name = 'testLoginScreen',attachment_type=AttachmentType.PNG)
            self.driver.close()


#pytest -v -s --alluredir="C:\Users\junaid\PycharmProjects\Demo\Reports" pytestdemo\test_example.py
