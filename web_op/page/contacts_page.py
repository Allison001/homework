from time import sleep

from web_op.page.basepage import BasePage
from web_op.page.creat_party_page import CreatParty


class ContactPage(BasePage):
    def goto_creat_page(self):
        self.find("class","member_colLeft_top_addBtn").click()  #点击+号
        self.find("class","js_create_party").click()
        return CreatParty(self.driver)


    # def get_party_list(self):
    #     pary_list = self.finds("xpath", '//*[@aria-level="3"]')
    #     parys = []
    #     for i in pary_list:
    #         parys.append(i.text)
    #     return parys