from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.XPATH,"//input[@name='uid']")
    password_field = (By.XPATH,"//input[@name='password']")
    login_button = (By.XPATH,"//input[@name='btnLogin']")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def set_username(self, username):
        self.set(self.username_field, username)
        
    def set_password(self, password):
        self.set(self.password_field, password)
        
    def click_login(self):
        self.click(self.login_button)
    
    def log_into_application(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def get_alert_message(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept() 
            return alert_text
        except TimeoutException:
            return None
        
    # def refresh(self):
    #     self.driver.refresh()
    #     WebDriverWait(self.driver, 10).until(EC.url_to_be(self.url))
    