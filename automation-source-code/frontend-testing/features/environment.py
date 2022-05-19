import os
import sys

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from selenium import webdriver

def before_all(context):
    context.frontend_url = context.config.userdata['frontend_url']


def before_scenario(context, scenario):
    browser          = context.config.userdata['browser']
    language         = context.config.userdata['language']
    context.language = language
    
    if browser == 'firefox':
        context.driver = webdriver.Firefox(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/firefoxWebDriver")
    elif browser == 'chrome':
        if(language == 'pt'):
            browser_language = {'intl.accept_languages': 'pt_BR'}
        else:
            browser_language = {'intl.accept_languages': 'en_US'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', browser_language)
        context.driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.realpath(__file__)) + "/resources/chromeDriver", options=options)


def after_scenario(context, scenario):
    context.driver.quit()