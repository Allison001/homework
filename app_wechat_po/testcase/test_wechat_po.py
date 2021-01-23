import pytest
import yaml

from app_wechat_po.page.app import App


def get_datas():
    with open('../data/wecaht_data.yaml',encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        data = datas["add"]
        ids = datas["idss"]
        return [data,ids]

class TestWechat():
    def setup(self):
        self.app = App()
        self.main = self.app.start_app().goto_main()

    def teardown(self):
        self.app.close_app()
    @pytest.mark.parametrize("name,gender,phone,email",get_datas()[0],ids=get_datas()[1])
    def test_wechat(self,name,gender,phone,email):
        elel = self.main.goto_member_list().goto_add_member().goto_add_member_detail().edit_name(name).edit_gender(gender).edit_phone(phone).edit_email(email).save().get_toast()

        assert elel=="添加成功"