from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_frame.basepage import BasePage
from app_frame.page.market import Market


class Main(BasePage):

    def goto_market(self):
        self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']"))

        # ele = (By.XPATH,"//*[@text='行情']")
        # wait = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(ele))
        # wait.click()

        self.find_and_click((By.XPATH,"//*[@text='行情']"))
        return Market(self.driver)
