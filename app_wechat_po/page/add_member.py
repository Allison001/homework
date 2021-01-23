from appium.webdriver.common.mobileby import MobileBy

from app_wechat_po.page.add_member_detail import AddMemberDetail
from app_wechat_po.page.basepage import BasePage


class AddMember(BasePage):
    def goto_add_member_detail(self):
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.find_and_click((MobileBy.XPATH,'//*[@text="手动输入添加"]'))
        return AddMemberDetail(self.driver)

    def get_toast(self):
        # ele = self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']").text
        ele = self.find_text((MobileBy.XPATH,"//*[@text='添加成功']"))
        return ele