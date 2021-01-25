import yaml
from selenium.webdriver.common.by import By

#装饰器，处理黑名单
def handle_black(fun):
    def ran(*args,**kwargs):
        instance = args[0]
        #获取黑名单
        # basck_list = [(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        with open("../black_list.yaml","r",encoding='UTF-8') as f:
            basck_list = yaml.load(f)
        #捕获异常（元素没找到）
        try:
            return fun(*args,**kwargs)

        except Exception as e:
            #遍历黑名单，如果发现黑名单中的元素存在，就对他进行处理
            for black in basck_list:
                eles = instance.driver.find_elements(*black)
                if len(eles) > 0:
                    #通过点击的方式，关闭弹窗
                    eles[0].click()
                    #再次查找
                    # return instance.find(*args,**kwargs)
                    return fun(*args,**kwargs)
            raise e
    return ran
