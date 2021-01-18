from time import sleep

import pytest
from appium import webdriver


class Test_demo():
    def setup(self):
        elel = {
            "platformName": "android",
            "deviceName": "78a0494b",
            "appPackage ": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", elel)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_a(self):
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        sleep(1)
        # self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        #输入姓名
        el5 = self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText")
        el5.send_keys("test2")
        #选择性别
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_xpath('//*[@text="女"]').click()
        #输入手机号码
        el7 = self.driver.find_element_by_xpath('//*[@text="手机号"]')
        el7.send_keys("13211111112")
        #输入邮箱
        el8=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.EditText")
        el8.send_keys("124@123.com")
        sleep(3)
        #点击保存按钮
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/ie7"]').click()
        #获取toast提示
        ele = self.driver.find_element_by_xpath("//*[@text='添加成功']").text
        assert "添加成功" == ele

if __name__ == '__main__':
    pytest.main()