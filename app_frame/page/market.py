import yaml
from selenium.webdriver.common.by import By

from app_frame.basepage import BasePage
from app_frame.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.run_step('../page/market.yaml','goto_search')

        # self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return Search(self.driver)
