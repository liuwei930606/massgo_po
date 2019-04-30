from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver = driver

    # 查找单个元素方法
    def base_find_element(self,feature,timeout=30,poll=0.5):
        by,value = feature
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(by,value))

    # 查找一组元素方法
    def base_find_elements(self, feature, timeout=30, poll=0.5):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    # 点击方法
    def base_click(self,feature):
        self.base_find_element(feature).click()

    # 输入方法
    def base_send_keys(self,feature,value):
        el = self.base_find_element(feature)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self,feature):
        return self.base_find_element(feature).text

    # 返回方法
    def base_back(self):
        self.driver.press_keycode(4)
