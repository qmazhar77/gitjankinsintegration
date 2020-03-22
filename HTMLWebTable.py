from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").submit()
driver.find_element_by_link_text("Admin").click()
row = (driver.find_element_by_xpath("//body//tbody//tr[1]"))
col = (driver.find_element_by_xpath("//body//th[1]"))
print ("Number of Row :", row)
print ("Number of Col :", col)

for r in range(2,row+1):
    for c in range(1,col+1):
        value = driver.find_element_by_xpath("//body//tbody//tr[1]").text
        print(value,end=" ")
        print()
driver.close()