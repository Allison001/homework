from time import sleep

from web_op.page.basepage import BasePage
from web_op.page.contacts_page import ContactPage
from web_op.page.creat_party_page import CreatParty


class MainPage(BasePage):

    def goto_contacts(self):
        self.find("id","menu_contacts").click()
        sleep(5)
        return ContactPage(self.driver)