import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def testlogin():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.demo.guru99.com/V4/")
    driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr559247")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("AjebyrU")
    driver.find_element(By.XPATH,"//input[@name='btnLogin']").click()
    title = driver.title
    assert title == "Guru99 Bank Manager HomePage"
    print(title)
    driver.quit()
