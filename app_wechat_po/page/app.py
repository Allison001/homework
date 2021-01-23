

#启动APP、重启APP、关闭APP、进入主页面
from appium import webdriver

from app_wechat_po.page.basepage import BasePage
from app_wechat_po.page.main import Main


class App(BasePage):

    def start_app(self):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = "Android"
            desired_caps['deviceName'] = "78a0494b"
            # desired_caps['app'] = os.path.abspath('/Users/a58/Downloads/zhuanzhuan_market_923.apk')
            desired_caps['appPackage'] = "com.tencent.wework"
            desired_caps['appActivity'] = "com.tencent.wework.launch.WwMainActivity"
            desired_caps['noReset'] = True
            desired_caps['ensureWebviewsHavePages'] = True
            # desired_caps['skipDeviceInitialization'] = 'true'
            desired_caps['settings[waitForIdleTimeout]'] = 1


            capb = {
                "platformName": "android",
                "deviceName": "78a0494b",
                "appPackage ": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": "true",
                'ensureWebviewsHavePages':"true",
                # "dontStopAppOnReset": True,
                # "skipDeviceInitialization": True,
                'settings[waitForIdleTimeout]' : 1
            }

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capb)
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