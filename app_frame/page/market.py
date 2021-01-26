import yaml
from selenium.webdriver.common.by import By

from app_frame.basepage import BasePage
from app_frame.page.search import Search


class Market(BasePage):
    def goto_search(self):
        #yaml的读取
        with open('../page/market.yaml','r',encoding='UTF-8') as f:
            data = yaml.load(f)
            #遍历每个动作
            for i in data:
                action = i['action']
                #如果动作是find_and_click,调用basepage中的find_and_click
                if action == 'find_and_click':
                    #调用find_and_click,并传入相应参数
                    self.find_and_click(i["locator"])

        # self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return Search(self.driver)
