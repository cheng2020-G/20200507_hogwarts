import pytest
import yaml
import allure
from unit.calc import Calc


class TestCalc:
    @allure.feature("计算器")
    def setup(self):
        self.calc = Calc()

    # yaml参数化
    @allure.story("加法")
    @pytest.mark.parametrize(["a", "b", "c"],
                             yaml.safe_load(open("D:/PycharmProject/20200507_pytest_calc/data/data.yaml")))
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        assert result == c

    @allure.story("除法")
    @pytest.mark.parametrize(["a", "b", "c"],
                             yaml.safe_load(open("D:/PycharmProject/20200507_pytest_calc/data/data1.yaml")))
    def test_div(self, a, b, c):
        result = self.calc.div(a, b)
        assert result == c


if __name__ == '__main__':
    pytest.main()
