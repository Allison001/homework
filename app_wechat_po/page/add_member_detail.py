from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_wechat_po.page.basepage import BasePage


class AddMemberDetail(BasePage):
    def edit_name(self,name):
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find_and_send_keys((MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText"),name)
        return self

    def edit_gender(self,gender):
        local= (MobileBy.XPATH,"//*[@text='男']")
        ele = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(local))
        ele.click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()

        if gender == "男":
            # self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
            self.find_and_click((MobileBy.XPATH,"//*[@text='男']"))
        elif gender == "女":
            # self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        return self

    def edit_phone(self,phone):
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="手机号"]').send_keys(phone)
        self.find_and_send_keys((MobileBy.XPATH,'//*[@text="手机号"]'),phone)
        return self

    def edit_email(self,email):
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'邮箱')]/../android.widget.EditText").send_keys(email)
        self.find_and_send_keys((MobileBy.XPATH,"//*[contains(@text,'邮箱')]/../android.widget.EditText"), email)
        return self

    def save(self):
        from app_wechat_po.page.add_member import AddMember
        # self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/ie7"]').click()
        self.find_and_click((MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/ie7"]'))
        return AddMember(self.driver)
