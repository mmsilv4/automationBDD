from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    title_label    = (By.ID, "")
    login_field    = (By.ID, "email")
    password_field = (By.ID, "password")
    btn_login      = (By.XPATH, "//span[@class='button__text'][text()='Entrar']")


    def set_login(self, login):
        super().type_in(self.login_field, login)
    

    def set_password(self, password):
        super().type_in(self.password_field, password)
    

    def click_btn_login(self):
        super.pause(2)
        super.click(self.btn_login)