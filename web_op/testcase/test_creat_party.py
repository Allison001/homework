from web_op.page.main_page import MainPage


class TestCreatParty():
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    def test_creat_party(self):
        result = self.main.goto_contacts().goto_creat_page().creat_party()
        assert result == True