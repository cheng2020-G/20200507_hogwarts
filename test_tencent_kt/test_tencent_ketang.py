import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


class TestTencentKeTang():
    def setup(self):
        chrome_option = Options()
        chrome_option.debugger_address = '127.0.0.1:9666'
        option_w3c = webdriver.ChromeOptions()
        option_w3c.add_experimental_option('w3c', False)
        # 复用浏览器
        # self.driver = webdriver.Chrome(options=chrome_option)
        # 不复用
        self.driver = webdriver.Chrome(options=option_w3c)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_tencent_login(self):
        self.driver.get("https://ke.qq.com/")
        ele_login = self.driver.execute_script("return document.getElementById('js_login')")
        ele_login.click()
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/a[2]").click()
        sleep(3)
        # print(self.driver.get_cookies())
        # self.driver.get("https://ke.qq.com/")
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.get("https://ke.qq.com/")
        db.close()
        ele_person = self.driver.find_element_by_xpath("//*[@id='js_logout_outer']/p/a/img")
        ele_logout = self.driver.find_element_by_xpath("//*[@id='js_logout_outer']/ul/li[last()]/a")
        action = ActionChains(self.driver)
        action.move_to_element(ele_person).perform()
        # action.drag_and_drop(ele_person, ele_logout)
        action.click(ele_logout).perform()
        sleep(3)
