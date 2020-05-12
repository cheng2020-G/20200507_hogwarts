import selenium
from selenium import webdriver
from time import sleep


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(3)
    driver.close()
