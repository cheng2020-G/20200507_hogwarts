from selenium import webdriver


class TestHogwarts():
    # 定义setup方法，初始化driver,get
    def setup(self):
        # 初始化driver,可以用chrome Firefox IE 等
        # 如果没有配置环境变量，可以用executable_path="driver path",例如：
        # self.driver = webdriver.Chrome(executable_path="D:/chromedriver_win32")
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        # 窗口最大化
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)

    # 定义teardown方法，执行用例后退出
    def teardown(self):
        self.driver.quit()
    # 定义测试case，里面包含测试步骤，定位元素的方式（八种），要执行什么操作，比如click,send等
    def test_hogwarts(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[2]/div/ul/li[4]/a").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
        self.driver.find_element_by_css_selector(
            "div.topic:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)").click()
