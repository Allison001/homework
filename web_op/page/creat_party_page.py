from time import sleep

from web_op.page.basepage import BasePage


class CreatParty(BasePage):
    def creat_party(self):
        self.find("css",'#__dialog__MNDialog__ > div > div.qui_dialog_body.ww_dialog_body > div > form > div:nth-child(1) > input').send_keys("Test1")
        sleep(3)
        #定位到弹窗上
        self.find("css","#__dialog__MNDialog__ > div > div.qui_dialog_body.ww_dialog_body").click()
        sleep(3)
        #z展开列表
        self.find("css","#__dialog__MNDialog__ > div > div.qui_dialog_body.ww_dialog_body > div > form > div:nth-child(3) > a > span.js_parent_party_name").click()
        sleep(3)
        #选择列表上得部门
        self.find("css",".qui_dialog_body.ww_dialog_body [id='1688853531101396_anchor']").click()
        sleep(3)
        #点击确定按钮
        self.find("css","#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue").click()
        sleep(3)

        # def get_party_list(self):
        pary_list = self.finds("xpath",'//*[@aria-level="3"]')
        parys = []
        for i in pary_list:
            parys.append(i.text)
        return parys


    def creat_party_fril(self):
        self.find("css",'#__dialog__MNDialog__ > div > div.qui_dialog_body.ww_dialog_body > div > form > div:nth-child(1) > input').send_keys("Test1")
        sleep(3)
        #定位到弹窗上
        self.find("css","#__dialog__MNDialog__ > div > div.qui_dialog_body.ww_dialog_body").click()
        sleep(3)
        #z展开列表
        self.find("css","#__dialog__MNDialog__ > div > div.qui_dialog_body.ww_dialog_body > div > form > div:nth-child(3) > a > span.js_parent_party_name").click()
        sleep(3)
        #选择列表上得部门
        self.find("css",".qui_dialog_body.ww_dialog_body [id='1688853531101396_anchor']").click()
        sleep(3)
        #点击确定按钮
        self.find("css","#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue").click()
        sleep(3)

        # def get_party_list(self):
        pary_list = self.finds("xpath",'//*[@aria-level="3"]')
        parys = []
        for i in pary_list:
            parys.append(i.text)
        return parys


