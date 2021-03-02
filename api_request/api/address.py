import requests

from api_request.api.base import Base


class Address(Base):

    # def __init__(self):
    #     # 获取token
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww045168ae97ffe137&corpsecret=nv7UxbjQ7DoSSbfFsh8qhft0KrA-D8R5FgE0KARIvec"
    #     r = self.send("get",url)
    #     self.token = r["access_token"]

    # 创建成员
    def add_member(self,userid:str,name:str,mobile:str,department:list,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        body = {"userid": userid, "name": name, "mobile": mobile, "department":department}
        body.update(**kwargs)
        return  self.send("post",url,json=body)


    # 查询成员
    def search_member(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        return self.send("get",url)


    # 更新成员
    def update_member(self,userid:str,name:str,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        body = {"userid": userid, "name": name}
        body.update(**kwargs)
        return self.send("post",url,json=body)


    # 删除成员
    def delete_member(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        return self.send("get",url)


