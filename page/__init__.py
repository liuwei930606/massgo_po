from selenium.webdriver.common.by import By


# 以下为信息页面配置信息

# 新建信息按钮
msg_new_msg_button = By.ID,'com.android.mms:id/action_compose_new'
# 联系人输入框
msg_input_contact_name = By.XPATH,'//*[@text = "接收者"]'
# 信息输入框
msg_input_msg_text = By.XPATH , '//*[@text = "键入信息"]'
# 发送信息按钮
msg_send_button = By.ID  , 'com.android.mms:id/send_button_sms'
# 信息发送内容获取
msg_send_msg_text = By.ID , 'com.android.mms:id/text_view'