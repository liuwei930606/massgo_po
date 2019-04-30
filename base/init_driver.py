from appium import webdriver


def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = 'com.android.mms'
    desired_caps['appActivity'] = '.ui.ConversationList'
    desired_caps['noReset'] = True
    # 声明我们的driver对象
    return  webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)