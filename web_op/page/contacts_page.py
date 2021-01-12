from time import sleep

from web_op.page.basepage import BasePage
from web_op.page.creat_party_page import CreatParty


class ContactPage(BasePage):
    def goto_creat_page(self):
        self.driver.find_element_by_class_name("member_colLeft_top_addBtnWrap js_create_dropdown").click()
        self.driver.find_element_by_link_text("添加部门").click()
        sleep(10)
        return CreatParty()