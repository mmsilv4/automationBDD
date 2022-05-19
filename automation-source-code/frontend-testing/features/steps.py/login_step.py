import os
import sys

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


from pages.login_page import LoginPage
from pages.base_page import Basepage


@step('The login was successful with {user} and {password}')
def step_impl(context, user, password):
    context.page_object = LoginPage(context.driver)
    context.page_object.pause()
    context.page_object.set_login(user)
    context.page_object.set_password(password)
    context.page_object.click_btn_login()