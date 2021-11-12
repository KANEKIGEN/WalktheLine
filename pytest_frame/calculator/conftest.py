import pytest
import yaml


def get_data():
    with open("../datas/data.yaml", "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


@pytest.fixture(params=get_data()['add']['P0']['datas'], ids=get_data()['add']['P0']['ids'])
def add_PO_data(request):
    return request.param


@pytest.fixture(params=get_data()['add']['P1_1']['datas'], ids=get_data()['add']['P1_1']['ids'])
def add_P1_1_data(request):
    return request.param


@pytest.fixture(params=get_data()['add']['P1_2']['datas'], ids=get_data()['add']['P1_2']['ids'])
def add_P1_2_data(request):
    return request.param


@pytest.fixture(params=get_data()['add']['P2']['datas'], ids=get_data()['add']['P2']['ids'])
def add_P2_data(request):
    return request.param


@pytest.fixture(params=get_data()['div']['P0']['datas'], ids=get_data()['div']['P0']['ids'])
def div_P0_data(request):
    return request.param


@pytest.fixture(params=get_data()['div']['P1_1']['datas'], ids=get_data()['div']['P1_1']['ids'])
def div_P1_1_data(request):
    return request.param


@pytest.fixture(params=get_data()['div']['P2']['datas'], ids=get_data()['div']['P2']['ids'])
def div_P2_data(request):
    return request.param


def pytest_collection_modifyitems(items: list):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
