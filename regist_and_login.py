from selenium import webdriver 
import time

def regist():
    driver = webdriver.Chrome() # web driver and browser used
    driver.maximize_window() # to maximize the size of the web to be tested
    driver.get("https://exoticls.com/") # the web link that we use as testing 
    time.sleep(2) # give a time lag of 2 seconds
    
    driver.get("https://exoticls.com/User/login") # login web link
    driver.find_element_by_xpath('/html/body/section/article/div/span[2]/a').click() # enter the register section with the button
    driver.find_element_by_id("reg_id").send_keys("metropolish") # enter the ID, in the syntax send_keys
    driver.find_element_by_id("email").send_keys("dummys123@gmail.com") # enter the EMAIL  
    driver.find_element_by_id("reg_password").send_keys("reaper12") # enter the password
    driver.find_element_by_id("nickName").send_keys("XSR") # enter the Nickname
    driver.find_element_by_name("ctl02").click() # button register
    
    # login field
    driver.find_element_by_id("login_id").send_keys("metropolish") # enter the id according to the one you registered earlier
    driver.find_element_by_id("login_password").send_keys("reaper12") # enter the password according to the one you registered earlier
    driver.find_element_by_name("ctl01").click() # button login 
    time.sleep(2) # give a time lag of 2 seconds
    driver.close() # close window browser

regist()
