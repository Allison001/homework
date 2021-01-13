import json

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

"""Mac中浏览器需要输入：/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome -remote-debugging-port=9222
window中浏览器需要输入：chrome --remote-debugging-port=9222
"""


class BasePage():

    def __init__(self,driver:WebDriver=None):

        bro = webdriver.ChromeOptions()
        bro.debugger_address = "127.0.0.1:9222"
        if driver is None:
            self.driver = webdriver.Chrome(options=bro)
            self._cookie_login()
            self.driver.maximize_window()
        else:
            self.driver = driver

        self.driver.implicitly_wait(10)


    def _cookie_login(self):
        # self.driver.get("https://work.weixin.qq.com/")
        # cookies = self.driver.get_cookies()
        # with open("cookies.json","w") as f:
        #     json.dump(cookies,f)


        self.driver.get("https://work.weixin.qq.com/")
        with open("cookies.json","r") as f:
            cookes = json.load(f)
        #注入cookies
        for i in cookes:
            self.driver.add_cookie(i)
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()

    def find(self,by,location):
        if by == "class":
            return self.driver.find_element_by_class_name(location)
        elif by == "name":
            return self.driver.find_element_by_name(location)
        elif by == "tag":
            return self.driver.find_element_by_tag_name(location)
        elif by == "id":
            return self.driver.find_element_by_id(location)
        elif by == "part":
            return self.driver.find_element_by_partial_link_text(location)
        elif by == "text":
            return self.driver.find_element_by_link_text(location)
        elif by == "css":
            return self.driver.find_element_by_css_selector(location)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(location)

    def finds(self,by,location):
        if by == "css":
            return self.driver.find_elements_by_css_selector(location)
        elif by == "name":
            return self.driver.find_elements_by_name(location)
        elif by == "class":
            return self.driver.find_elements_by_class_name(location)
        elif by == "tag":
            return self.driver.find_elements_by_tag_name(location)
        elif by == "part":
            return self.driver.find_elements_by_partial_link_text(location)
        elif by == "link":
            return self.driver.find_elements_by_link_text(location)
        elif by == "id":
            return self.driver.find_elements_by_id(location)
        elif by == "xpath":
            return self.driver.find_elements_by_xpath(location)