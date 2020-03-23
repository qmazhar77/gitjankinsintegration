from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").submit()
#admin = driver.find_element_by_link_text("Admin")
admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermang = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermang).move_to_element(user).click().perform()
time.sleep(10)
driver.close()


driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)
actions.double_click(element).perform() # perfoming souble click
time.sleep(10)
driver.close()

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(button).perform() # Right click action
time.sleep(10)
driver.close()

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source_element = driver.find_element_by_xpath("//*[@id='box3']")
target_elemet = driver.find_element_by_xpath("//*[@id='box103']")

actions = ActionChains(driver)
actions.drag_and_drop(source_element,target_elemet).perform()
time.sleep(10)
driver.close()