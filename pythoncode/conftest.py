import os

import pytest
import yaml

from pythoncode.Calculator import Calculator


@pytest.fixture(scope="module")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("计算结束")

# 通过os.path.driname获取当前文件的路径，拼接"/cal.yaml"获取文件的绝对路径
file_name = os.path.dirname(__file__) + "/cal.yaml"
with open(file_name) as f:
    data = yaml.safe_load(f)
    add_data = data["adds"]
    add_ids = data["idsa"]
    sub_data = data["sub"]
    sub_ids = data["idsb"]
    mul_data = data["mul"]
    mul_ids = data["idsc"]
    div_data = data["div"]
    div_idsd = data["idsd"]




@pytest.fixture(params=add_data,ids=add_ids)
def get_datas_add(request):
    datass = request.param
    yield datass

@pytest.fixture(params=sub_data,ids=sub_ids)
def get_datas_sub(request):
    subdatas = request.param
    yield subdatas

@pytest.fixture(params=mul_data,ids=mul_ids)
def get_datas_mul(request):
    muldatas = request.param
    yield  muldatas

@pytest.fixture(params=div_data,ids=div_idsd)
def get_datas_div(request):
    divdatas = request.param
    yield divdatas