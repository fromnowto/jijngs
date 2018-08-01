import os,sys
sys.path.append(os.getcwd())
#
import allure
import pytest
# import yaml
# class Read_data:
#     def __init__(self,path_name):
#         self.flie_path = "." + os.sep + path_name
#     def get_datas(self):
#         with open(self.flie_path, "r") as f:
#             return yaml.load(f)
#
# def get_data():
#     ls=[]
#     data = Read_data("data_1.yml").get_datas()
#     for i in data.get("data").values():
#         ls.append((i.get("a"),i.get("b")))
#     return ls

class Test_1():
    # @allure.step(title="这是个登录方式")
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @pytest.mark.parametrize("a,b",[(2,2),(3,4)])
    def test_001(self,a,b):
        allure.attach("输入用户名",str(a))
        print("\n----test001")
        allure.attach("输入密码",str(b))

        assert a == b
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_002(self):
        allure.attach("输入用户名","afga")
        print("\n----test002")
        allure.attach("输入密码","83491")
        assert 0

