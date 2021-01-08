import json
from selenium import webdriver


class Test_qiyewechat:
    def setup(self):
        browser_copy = webdriver.ChromeOptions()
        browser_copy.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=browser_copy)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_qywechat(self):
        #获取cookie并添加到json文件中
        cookies = self.driver.get_cookies()
        with open("cookies.json","w") as f:
            json.dump(cookies,f)

        #打开要访问的网站，并将cookie添加到网站上
        self.driver.get("https://work.weixin.qq.com/")
        with open("cookies.json","r") as f:
            cookiees = json.load(f)
        for i in cookiees:
            self.driver.add_cookie(i)

        #打开完整登录后的首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        #点击顶部客户联系tab
        self.driver.find_element_by_id("menu_customer").click()


