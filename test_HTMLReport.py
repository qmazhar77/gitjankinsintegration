from selenium import webdriver
import pytest

class Test_OrangeHRM():
    @pytest.fixture()
    def setup(self):
        global driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        yield
        self.driver.close()


    def test_homePageTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title=="OrangeHRM123"

    def test_Login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").submit()
        assert self.driver.title=="OrangeHRM"

#pytest -v -s --html=.\htmlreport\report.html --self-contained-html pytestDemo/test_htmlreport.py
#"html=.\htmlreport\report.html" HTML report will created in spacified folder which is "htmlreport"
