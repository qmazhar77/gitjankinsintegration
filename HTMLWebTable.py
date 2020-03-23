from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").submit()
driver.find_element_by_link_text("Admin").click()
rows = len(driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr[1]/td"))
print("No of rows: ", rows)
print("No of Col:", cols)


for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end="              ")
    print()
driver.close()