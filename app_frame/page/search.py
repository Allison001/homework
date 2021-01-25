from selenium.webdriver.common.by import By

from app_frame.basepage import BasePage


class Search(BasePage):

    def search(self):
        self.find_and_send_keys((By.XPATH,"//*[@text='拥抱产业风口，智能汽车ETF（515250）']"),"alibaba")
        ele = self.find((By.XPATH,"//*[@text='阿里巴巴概念']")).text
        return ele