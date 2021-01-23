from appium.webdriver.common.mobileby import MobileBy

from app_wechat_po.page.basepage import BasePage
from app_wechat_po.page.member_list import MemberList


class Main(BasePage):
    def goto_member_list(self):
        # self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.find_and_click((MobileBy.XPATH,'//*[@text="通讯录"]'))
        return MemberList(self.driver)