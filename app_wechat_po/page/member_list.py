from appium.webdriver.common.mobileby import MobileBy

from app_wechat_po.page.add_member import AddMember
from app_wechat_po.page.basepage import BasePage


class MemberList(BasePage):
    def goto_add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.scroll_click("添加成员")
        return AddMember(self.driver)