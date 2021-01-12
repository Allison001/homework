import json

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self,driver:WebDriver=None):
        bro = webdriver.ChromeOptions()
        bro.debugger_address = "127.0.0.1:9222"
        if driver is None:
            self.driver = webdriver.Chrome(options=bro)
        else:
            self.driver = driver
        self._cookie_login()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        cookies = self.driver.get_cookies()
        with open("cookies.json","w") as f:
            json.dump(cookies,f)


        self.driver.get("https://work.weixin.qq.com/")
        with open("cookies.json","r") as f:
            cookes = json.load(f)
        #注入cookies
        for i in cookes:
            self.driver.add_cookie(i)


