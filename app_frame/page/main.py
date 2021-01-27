import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_frame.basepage import BasePage
from app_frame.page.market import Market


class Main(BasePage):

    def goto_market(self):
        self.run_step("../page/main.yaml",'goto_market')

        # self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']"))
        # self.find_and_click((By.XPATH,"//*[@text='行情']"))
        return Market(self.driver)

    def goto_my(self):
        self.run_step('../page/main.yaml','goto_my')