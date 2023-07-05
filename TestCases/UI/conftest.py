# conftest.py
# ����һ��conftest�ļ���pytest������ִ�д��ļ��з���
import pytest

# ����һ��ȫ�ֱ��������ڴ洢����ִ�й����е�����
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