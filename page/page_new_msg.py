from base.base_action import BaseAction
import page


class PageNewMsg(BaseAction):
    # 输入联系人姓名
    def page_input_contact_name(self, name):
        self.base_send_keys(page.msg_input_contact_name,name)

    # 输入要发送信息
    def page_input_msg_content(self, content):
        self.base_send_keys(page.msg_input_msg_text,content)

    # 点击发送按钮
    def page_click_send_button(self):
        self.base_click(page.msg_send_button)