import requests
import json

#获取token
url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww045168ae97ffe137&corpsecret=nv7UxbjQ7DoSSbfFsh8qhft0KrA-D8R5FgE0KARIvec"
r = requests.get(url)
token = r.json()["access_token"]

#创建成员
url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
body = {"userid": "zhangsan","name": "张三","mobile": "+86 13800000001","department": [1]}
r = requests.post(url,json=body)
print(r.json())

#查询成员
url =f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=zhangsan"
r = requests.get(url)
print(r.json())


#更新成员
url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
body = {"userid": "zhangsan","name": "李四"}
r = requests.post(url,json=body)
print(r.json())


#删除成员
url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
r = requests.get(url)
print(r.json())
