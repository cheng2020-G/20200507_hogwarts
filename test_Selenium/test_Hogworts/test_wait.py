from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # 显式等待，方法一
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_selected(
            (By.CSS_SELECTOR, '//*[@id="main-page"]/div[1]/nav/div/ul[1]/li[1]/a')))
        self.driver.find_element_by_css_selector(
            "ul.navbar-nav:nth-child(1) > li:nth-child(4) > a:nth-child(1)").click()

        # 显式等待，自定义wait方法
        def wait(x):
            return len(
                self.driver.find_element_by_css_selector('//*[@id="main-page"]/div[1]/nav/div/ul[1]/li[1]/a')) == 1
        # python传参一定不要带括号，带括号就成了调用，用wait传参，而不是wait（）或者wait（x）
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element_by_css_selector('ul.navbar-nav:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()