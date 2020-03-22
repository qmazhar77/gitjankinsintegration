from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
#driver.save_screenshot("D:\Azhar Python\googlepage.png")
driver.get_screenshot_as_file("D:\Azhar Python\googlepage1.png")