import yaml
from selenium.webdriver.common.by import By

from app_frame.basepage import BasePage


class Search(BasePage):

    def search(self):

        #yaml的读取
        with open('../page/search.yaml','r',encoding='UTF-8') as f:
            data = yaml.load(f)
            #遍历每个动作
            for i in data:
                action = i['action']
                #如果动作是find_and_click,调用basepage中的find_and_click
                if action == 'find_and_click':
                    #调用find_and_click,并传入相应参数
                    self.find_and_click(i["locator"])
                elif action=="find_and_send_keys":
                    self.find_and_send_keys(i["locator"],i["content"])
                elif action =="find":
                    ele = self.find(i["locator"]).text
                    return ele

        # self.find_and_send_keys((By.XPATH,"//*[@text='大数据ETF（515400）聚焦国家大数据战略']"),"alibaba")
        # ele = self.find((By.XPATH,"//*[@text='阿里巴巴概念']")).text
        # return ele