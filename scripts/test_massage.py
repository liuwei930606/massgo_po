import pytest

from base.init_driver import init_driver
from page.page import Page


class TestMassage:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(('name','content') , [('180000000' , 'nihaonih'),('180000001' , 'nihao')])
    def test_massage(self,name,content):
        self.page.page_index_msg_obj.page_click_new_msg()
        self.page.page_new_msg_obj.page_input_contact_name(name)
        self.page.page_new_msg_obj.page_input_msg_content(content)
        self.page.page_new_msg_obj.page_click_send_button()
        assert self.page.page_sended_msg_obj.page_sended_msg_text() == content