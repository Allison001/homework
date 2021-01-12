import json
from time import sleep

from selenium import webdriver


class TestDemo:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def teardown_class(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookies.json","r") as f:
            cookes = json.load(f)
        #注入cookies
        for i in cookes:
            self.driver.add_cookie(i)
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()


        sleep(3)
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)
        self.driver.find_element_by_class_name("member_colLeft_top_addBtn").click()  #点击+号
        sleep(3)
        self.driver.find_element_by_class_name("js_create_party").click()
        sleep(10)
