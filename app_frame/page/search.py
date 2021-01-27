import yaml
from selenium.webdriver.common.by import By

from app_frame.basepage import BasePage


class Search(BasePage):

    def search(self):
        self.run_step("../page/search.yaml",'search')

        # self.find_and_send_keys((By.XPATH,"//*[@text='大数据ETF（515400）聚焦国家大数据战略']"),"alibaba")
        # ele = self.find((By.XPATH,"//*[@text='阿里巴巴概念']")).text
        # return ele