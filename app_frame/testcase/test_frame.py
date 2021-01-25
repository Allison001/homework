from app_frame.app import App


class TestFrame():

    def setup(self):
        self.app = App()
        self.main = self.app.start_app().goto_main()

    def teardown(self):
        self.app.close_app()

    def test_search(self):
        element = self.main.goto_market().goto_search().search()
        assert element == "阿里巴巴概念"