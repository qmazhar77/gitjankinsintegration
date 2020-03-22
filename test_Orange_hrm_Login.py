from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"webpage title is not matching")

    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").submit()
        self.assertEqual("OrangeHRM",self.driver.title,"wabpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print (" Test Completed")
if __name__=='__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\junaid\\PycharmProjects\\Demo\\PytestDemo\\testrunnerReport'))

#python pytestdemo\test_orange_hrm_login.py
#command need to run to generate testrunreport
