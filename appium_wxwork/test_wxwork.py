import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWxWork():
    # 类中只执行一次，作用域为当前类
    def setup_class(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1：7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": True,
            "unicodeKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    # 每个方法前运行，作用域为类中的每一个方法
    def setup(self):
        pass

    def teardown(self):
        pass

    # @pytest.mark.skip
    @pytest.mark.parametrize(["name", "phone"], yaml.safe_load(
        open('D:/PycharmProject/20200507_pytest_calc/selenium_wechat_po/data/add_contact.yaml')))
    def test_add_contact(self, name, phone):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='姓名　']/..//*[@class='android.widget.EditText']").send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机　']/..//*[@class='android.widget.EditText']").send_keys(
            phone)
        self.driver.find_element(MobileBy.XPATH, "//*[@resource_id='com.tencent.wework:id/gvk'] and //*[@='保存']").click()
