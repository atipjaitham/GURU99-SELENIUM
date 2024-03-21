import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utils.test_data import TestData



class TestLogin(BaseTest):
    
    @pytest.mark.parametrize("username, password", TestData.login_credentials())
    def test_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login()
        
        if username == "mngr559247" and password == "AjebyrU":
            actual_title = login_page.get_title()
            assert actual_title == "Guru99 Bank Manager HomePage"
            manager_id_element = login_page.find_manager_id_element(username)
            manager_id_text = manager_id_element.text # Retrieve the visible text from the web element and store it in manager_id_text variable
            print(manager_id_text)
            assert manager_id_text == f"Manger Id : {username}"
        else:
            actual_message = login_page.get_alert_message()
            print(actual_message)
            assert actual_message == "User or Password is not valid"

