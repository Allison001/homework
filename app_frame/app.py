

#启动APP、重启APP、关闭APP、进入主页面
from appium import webdriver

from app_frame.basepage import BasePage
from app_frame.page.main import Main


class App(BasePage):

    def start_app(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "78a0494b"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart_app(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def close_app(self):
        self.driver.quit()
        return self

    def goto_main(self)->Main:
        return Main(self.driver)