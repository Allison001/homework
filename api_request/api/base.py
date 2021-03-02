import requests


class Base():
    def __init__(self):
        # 获取token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww045168ae97ffe137&corpsecret=nv7UxbjQ7DoSSbfFsh8qhft0KrA-D8R5FgE0KARIvec"
        r = requests.get(url).json()
        self.token = r["access_token"]
        #声明一个session
        self.s = requests.session()
        #把token放入到session中
        self.s.params = {"access_token":self.token}


    def send(self,*args,**kwargs):

        #第一种写法
        #使用session
        r = self.s.request(*args,**kwargs)
        return r.json()

        #第二种写法
        # r = requests.request(method,url,**kwargs)
        # return r.json()

