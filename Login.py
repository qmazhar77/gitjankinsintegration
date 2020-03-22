from selenium import webdriver
import time
import unittest
import sys
import os
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from PytestDemo.Pages.loginPage import LoginPage
from PytestDemo.Pages.homePage import HomePage
class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def test_login1_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_Welcome()
        homepage.click_logout()

    def test_login_invalid_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element_by_xpath("").text
        self.assertEqual(message, "Invalid credentials")

        #self.driver.find_element_by_id("txtUsername").send_keys("admin")
        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_id("btnLogin").submit()
        #self.driver.find_element_by_id("welcome").click()
        #self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print ("Test comlited")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/junaid/PycharmProjects/Demo/PytestDemo/Reports'))

# for executing from command prompt give the full bath till pytestdemo if __name__ == '__main__' is not there
#python  -m unittest Login.py
#if  __name__ == '__main__' is there then write directly on command prompt following
#python Login.py

#C:\user\junaid\PycharmProjects\Demo> python -m PytestDemo.Login