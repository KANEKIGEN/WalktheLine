import sys

sys.path.append("../../")
import logging
import allure
import pytest

from pytest_frame.calculator.util.algorithm import add, div


@allure.feature("加法")
class TestAddCalculator:
    def setup_class(self):
        print("开始测试")

    def teardown_class(self):
        print("结束测试")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.ADD_P0
    @allure.title("加法001，002，003")
    def test_add_P0(self, add_PO_data):
        logging.info("加法P0开始运行测试")
        logging.info(f"数据{add_PO_data}")
        assert add_PO_data[2] == add(add_PO_data[0], add_PO_data[1])

    @pytest.mark.ADD_P1_1
    @allure.title("加法004-011")
    def test_add_P1_1(self, add_P1_1_data):
        logging.info("加法P1_1开始运行测试")
        logging.info(f"数据{add_P1_1_data}")
        assert add_P1_1_data[2] == add(add_P1_1_data[0], add_P1_1_data[1])

    @pytest.mark.ADD_P1_2
    @allure.title("加法012-017")
    def test_add_P1_2(self, add_P1_2_data):
        logging.info("加法P1_2开始运行测试")
        logging.info(f"数据{add_P1_2_data}")
        with pytest.raises(eval(add_P1_2_data[2])) as e:
            logging.info(f"异常{e}")
            add(add_P1_2_data[0], add_P1_2_data[1])
            assert add_P1_2_data[2] == e.type

    @pytest.mark.ADD_P2
    @allure.title("加法018-021")
    def test_add_P2(self, add_P2_data):
        logging.info("加法P2开始运行测试")
        logging.info(f"数据{add_P2_data}")
        with pytest.raises(eval(add_P2_data[2])) as e:
            logging.info(f"异常{e}")
            result = add(add_P2_data[0], add_P2_data[1])
            assert add_P2_data[2] == e.type

@allure.feature("除法")
class TestDivCalculator:
    @pytest.mark.DIV_P0
    @allure.title("除法001-004")
    def test_div_P0(self, div_P0_data):
        logging.info("除法P0开始运行测试")
        logging.info(f"数据{div_P0_data}")
        assert div_P0_data[2] == div(div_P0_data[0], div_P0_data[1])

    @pytest.mark.DIV_P1_1
    @allure.title("除法005-011")
    def test_div_P1_1(self, div_P1_1_data):
        logging.info("除法P1_1开始运行测试")
        logging.info(f"数据{div_P1_1_data}")
        with pytest.raises(eval(div_P1_1_data[2])) as e:
            div(div_P1_1_data[0], div_P1_1_data[1])
            assert div_P1_1_data[2] == e.typename

    @pytest.mark.DIV_P2
    @allure.title("除法012-015")
    def test_div_P2(self, div_P2_data):
        logging.info("除法P2开始运行测试")
        logging.info(f"数据{div_P2_data}")
        with pytest.raises(eval(div_P2_data[2])) as e:
            logging.info(f"异常{e}")
            result = div(div_P2_data[0], div_P2_data[1])
            assert div_P2_data[2] == e.type
