from time import sleep

from web_op.page.basepage import BasePage
from web_op.page.creat_party_page import CreatParty


class ContactPage(BasePage):
    def goto_creat_page(self):
        self.driver.find_element_by_class_name("member_colLeft_top_addBtn").click()  #点击+号
        self.driver.find_element_by_class_name("js_create_party").click()
        return CreatParty(self.driver)


    def get_party_list(self):
        pary_list = self.driver.find_elements_by_css_selector(".jstree-anchor")
        parys = []
        for i in pary_list:
            parys.append(i.text)
        return parys