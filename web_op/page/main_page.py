from time import sleep

from web_op.page.basepage import BasePage
from web_op.page.contacts_page import ContactPage


class MainPage(BasePage):

    def goto_contacts(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(5)
        return ContactPage(self.driver)
