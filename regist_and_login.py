from selenium import webdriver 
import time

def regist():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://exoticls.com/") 
    time.sleep(2)
    driver.get("https://exoticls.com/User/login")
    driver.find_element_by_xpath('/html/body/section/article/div/span[2]/a').click()
    driver.find_element_by_id("reg_id").send_keys("metropolish")
    driver.find_element_by_id("email").send_keys("dummys123@gmail.com")
    driver.find_element_by_id("reg_password").send_keys("reaper12")
    driver.find_element_by_id("nickName").send_keys("XSR")
    driver.find_element_by_name("ctl02").click()
    driver.find_element_by_id("login_id").send_keys("metropolish")
    driver.find_element_by_id("login_password").send_keys("reaper12")
    driver.find_element_by_name("ctl01").click() 
    time.sleep(2)
    driver.close()

regist()
