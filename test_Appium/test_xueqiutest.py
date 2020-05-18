import pytest
from appium import webdriver


class TestXueqiu():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1：7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_xueqiu_case01(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/code' and @text='09988']").click()
        ele_price = float(
            self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        assert ele_price > 200

    def test_xueqiu_caes02(self):
        ele_search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(ele_search.text)
        print(ele_search.location)
        print(ele_search.size)
        # 判断元素是否可用
        ele_search_enable =ele_search.is_enabled()
        # 判断元素是否可点击，如果可点击则点击
        if ele_search_enable == True:
            ele_search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            ele_alibaba = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/code' and @text='09988']")
            #元素是否可见
            ele_alibaba_display = ele_alibaba.get_attribute("displayed")
            if ele_alibaba_display == True:
                print("元素可以使用")
            else:
                print("元素不可使用")

