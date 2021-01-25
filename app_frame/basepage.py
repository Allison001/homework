from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from app_frame.handle_black import handle_black


class BasePage():
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    #黑名单处理
    @handle_black
    def find(self,location):
        return self.driver.find_element(*location)


    def find_and_click(self,location):
        self.find(location).click()

    def find_and_send_keys(self,location,text):
        self.find(location).send_keys(text)

    def scroll_click(self,text):
        elem = (MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')
        self.find_and_click(elem)

    def find_text(self,location):
        texts = self.find(location).text
        return texts