from base.base_action import BaseAction
import page


class PageSendedMsg(BaseAction):
    # 获取发送信息并返回
    def page_sended_msg_text(self):
        return self.base_get_text(page.msg_send_msg_text)