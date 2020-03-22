from selenium import webdriver
import logging

logging.basicConfig(filename='test1.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
#class logtest:
#    driver = webdriver.Chrome()
#    driver.get("https://www.google.com/")
#    driver.maximize_window()

#    try:
#        driver.find_element_by_id("name").click()
#    except Exception as e:
#        logging.debug("Element not found", e)
#        logging.debug("Hello")

#    logging.debug("azhar")
#    driver.close()

#logtest

#f = 5  # int(input("Enter the first number :"))
#s = 2  # int(input("Enter the seconf numer :"))

class testlog:
    def __init__(self,firstno):
        self.firstno = firstno
        logging.debug('Create Employee: {}'.format(self.firstno))

    @property
    def email(self):
        return '{}'.format(self.firstno)
try:
#    emp1= testlog(123)
    emp2= testlog("asdas")
    logging.debug("valid number")
except Exception as e:
    logging.debug("Invalid number", e)
#    try:
#        logging.debug("Resource Open")
#        Result = f / s
#        print("Total: ", Result)
#        k = int(input("enter the number"))
#        logging.debug (k)
#    except ZeroDivisionError as e:
#        print("You have entered invalid input", e)
    #except ValueError as e:
    #    print("invalid input", e)
#    except Exception as e:
#        print("Something went wrong", e)

#logging.debug("Resource Closed")