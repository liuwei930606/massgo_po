from page.page_index_msg import PageIndexMsg
from page.page_new_msg import PageNewMsg
from page.page_sended_msg import PageSendedMsg


class Page:
    def __init__(self,driver):
        self.driver = driver
        # 创建信息首页对象

    @property
    def page_index_msg_obj(self):
        return PageIndexMsg(self.driver)

    # 创建新建信息页对象
    @property
    def page_new_msg_obj(self):
        return PageNewMsg(self.driver)

    # 创建发送完信息页对象
    @property
    def page_sended_msg_obj(self):
        return PageSendedMsg(self.driver)