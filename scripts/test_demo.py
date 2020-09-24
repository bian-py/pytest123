from time import sleep

from selenium import webdriver

import os

import allure
import pytest


@allure.feature("这是feature功能描述")
class Test登录:
    @allure.story("这是story")
    @allure.description("这是description描述")
    @allure.title("这是title")
    def test01(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        sleep(5)
        driver.quit()
        print('这是第一个测试用例')
        assert 1 == 1
