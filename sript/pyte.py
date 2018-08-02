import os,sys
sys.path.append(os.getcwd())
import allure
import pytest
class Test_1():
    @allure.step(title="这是个登录方式")
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @pytest.mark.parametrize("a,b",[(2,2),(3,3)])
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
        assert 1

