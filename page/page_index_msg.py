from base.base_action import BaseAction
import page


class PageIndexMsg(BaseAction):
        def page_click_new_msg(self):
            self.base_click(page.msg_new_msg_button)