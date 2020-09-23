import os

import allure
import pytest


@allure.feature("这是feature功能描述")
class Test登录:
    @allure.story("这是story")
    @allure.description("这是description描述")
    @allure.title("这是title")
    def test01(self):
        print('这是第一个测试用例')
        assert 1 == 1

    @allure.story("这是story")
    @allure.description("这是description描述2")
    @allure.title("这是title2")
    def test02(self):
        print('这是第一个测试用例')
        assert 2 == 3


if __name__ == "__main__":
    pytest.main(['--alluredir', './temp',"-sv"])
    os.system("allure generate temp -o ./report --clean")
