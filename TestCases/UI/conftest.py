# conftest.py
# 这是一个conftest文件，pytest会有限执行此文件中方法
import pytest

# 定义一个全局变量，用于存储用例执行过程中的数据
data = {}

@pytest.fixture
def set_data():
    def _set_data(key, value):
        data[key] = value

    return _set_data


@pytest.fixture
def get_data():
    def _get_data(key):
        return data.get(key)

    return _get_data