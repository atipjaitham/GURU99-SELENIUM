import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert


class BasePage:
    """
    The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
    """
    def __init__(self, driver):
        self.driver = driver
        self.screenshot_path = "C:/Users/atipj/Documents/Portfolio/Guru99/Automation with Selenium/GURU99-SELENIUM/screenshots/"
        
    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self, locator, value):
        element = self.find(*locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def handle_alert_exception(self):
        try:
            alert = Alert(self.driver)
            alert.accept()
        except UnexpectedAlertPresentException:
            pass

    def click_right_menu_page(self, page_name):
        page = By.XPATH, f"//aside[@id='column-right']//a[text()='{page_name}']"
        self.click(page)

    def page(self, page_name):
        return By.XPATH, f"//aside[@id='column-right']//a[text()='{page_name}']"
  
    def find_manager_id_element(self, username):
        manager_id_locator = (By.XPATH, f"//td[contains(text(), 'Manger Id : {username}')]")
        return self.find(*manager_id_locator)
  
    def take_screenshot(self, filename):
        full_path = os.path.join(self.screenshot_path, filename)
        self.driver.save_screenshot(full_path)