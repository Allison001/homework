import pytest
import yaml

from pythoncode.Calculator import Calculator



class Test_Cala:

    #加法测试
    @pytest.mark.first
    def test_add(self,get_calc,get_datas_add):
        add = None
        try:
            add = get_calc.add(get_datas_add[0],get_datas_add[1])
            print(add)
            #防止小数过小与断言不相符
            if isinstance(add, float):
                add = round(add,2)
        except Exception as e:
            print(e)
        # assert add == get_datas_add[2]
        pytest.assume(add == get_datas_add[2])

    #除法测试
    @pytest.mark.fourth
    def test_div(self,get_calc,get_datas_div):
        div = None
        try:
            div = get_calc.div(get_datas_div[0],get_datas_div[1])
            print(div)
            if isinstance(div,float):
                div = round(div,2)
        except Exception as e:
            print(e)
        # assert div == get_datas_div[2]
        pytest.assume(div == get_datas_div[2])

    #减法测试
    @pytest.mark.second
    def test_sub(self,get_calc,get_datas_sub):
        sub = None
        try:
            sub = get_calc.sub(get_datas_sub[0],get_datas_sub[1])
            print(sub)
            if isinstance(sub,float):
                sub = round(sub,2)
        except Exception as e:
            print(e)
        # assert sub == get_datas_sub[2]?\
        pytest.assume(sub == get_datas_sub[2])

    #乘法测试
    @pytest.mark.third
    def test_mul(self,get_calc,get_datas_mul):
        mul = None
        try:
            mul = get_calc.mul(get_datas_mul[0],get_datas_mul[1])
            print(mul)
            if isinstance(mul,float):
                mul = round(mul,2)
        except Exception as e:
            print(e)
        # assert mul == get_datas_mul[2]
        pytest.assume(mul == get_datas_mul[2])


