import pytest
from api_request.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()


    @pytest.mark.parametrize("userid,name,mobile,dep",[("wangwu002","张一","15910720001",[1]),
                                                       ("wangwu003","张儿","15910720002",[2]),
                                                       ("wangwu004","张思","15910720003",[2])])
    def test_add_memeber(self,userid,name,mobile,dep):
        #清除数据
        self.address.delete_member(userid)

        #添加成员
        r = self.address.add_member(userid=userid,name=name,mobile=mobile,department=dep)
        assert r.get("errcode") == 0

        #查询成员
        r = self.address.search_member(userid)
        assert r.get("name","添加失败") == name

