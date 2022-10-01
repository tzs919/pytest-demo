import allure
import pytest
import random
import time


@allure.feature('test_xfail_expected_failure')
@pytest.mark.xfail(reason='该功能尚未实现')
def test_xfail_expected_failure():
    print("该功能尚未实现")
    assert False


@allure.feature('test_xfail_unexpected_pass')
@pytest.mark.xfail(reason='该Bug尚未修复')
def test_xfail_unexpected_pass():
    print("该Bug尚未修复")
    assert True


'''当条件为True则跳过执行'''


@allure.feature("test_skipif")
@pytest.mark.skipif(True, reason="如果操作系统是Mac则跳过执行")
def test_skipif():
    print("操作系统是Mac，test_skipif()函数跳过执行")


@allure.step
def simple_step(step_param1, step_param2=None):
    pass


@pytest.mark.parametrize('param1', [True, False], ids=['1', '2'])
def test_parameterize_with_id(param1):
    simple_step(param1)


@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['1', '2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step(param1, param2)


@allure.step("步骤二")
def passing_step():
    pass


@allure.step("步骤三")
def step_with_nested_steps():
    nested_step()


@allure.step("步骤四")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("步骤五")
def nested_step_with_arguments(arg1, arg2):
    pass


@allure.step("步骤一")
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()


@allure.title("断言2+2=4")
def test_with_a_title():
    assert 2 + 2 == 4


@allure.title("动态标题: {param1} + {param2} = {expected}")
@pytest.mark.parametrize('param1,param2,expected', [(2, 2, 4), (1, 2, 5)])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected


@allure.title("这是个动态标题，会被替换")
def test_with_dynamic_title():
    assert 2 + 2 == 4
    allure.dynamic.title('测试结束，做为标题')


@allure.link('https://www.cnblogs.com/mrjade/')
def test_with_link():
    pass


@allure.link('https://www.cnblogs.com/mrjade/', name='点击进入mrjade博客园')
def test_with_named_link():
    pass


@allure.issue('https://github.com/allure-framework/allure-python/issues/642', 'bug issue链接')
def test_with_issue_link():
    pass


@allure.testcase("https://www.cnblogs.com/mrjade/", '测试用例地址')
def test_with_testcase_link():
    pass


@allure.step
def passing_step():
    pass


@allure.step
def flaky_broken_step():
    if random.randint(1, 5) != 1:
        raise Exception('Broken!')


"""需安装【pip3 install pytest-rerunfailures】"""


@pytest.mark.flaky(reruns=3, reruns_delay=1)  # 如果失败则延迟1s后重试
def test_broken_with_randomized_time():
    passing_step()
    time.sleep(random.randint(1, 3))
    flaky_broken_step()


@pytest.fixture(scope="session")
def login_fixture():
    """需安装【pip3 install pytest-rerunfailures】"""
    print("前置登录")


@allure.step("步骤1")
def step_1():
    print("操作步骤1")


@allure.step("步骤2")
def step_2():
    print("操作步骤2")


@allure.step("步骤3")
def step_3():
    print("操作步骤3")


@allure.step("步骤4")
def step_4():
    print("操作步骤4")


@allure.epic("会员项目")
@allure.feature("登录")
class TestAllureALL:

    @allure.testcase("https://www.cnblogs.com/mrjade/", '测试用例,点我一下')
    @allure.issue("https://github.com/allure-framework/allure-python/issues/642", 'Bug 链接,点我一下')
    @allure.title("用户名错误")
    @allure.story("登录测试用例1")
    @allure.severity(allure.severity_level.TRIVIAL)  # 不重要的
    # @allure.severity(allure.severity_level.MINOR) # 轻微的
    # @allure.severity(allure.severity_level.BLOCKER)  # 阻塞的
    # @allure.severity(allure.severity_level.CRITICAL)  # 严重的
    # @allure.severity(allure.severity_level.NORMAL)  # 普通的
    def test_case_1(self):
        """
        公众号：测试工程师成长之路
        """
        print("测试用例1")
        step_1()
        step_2()

    @allure.title("用户名正确，密码错误")
    @allure.story("登录测试用例2")
    def test_case_2(self):
        print("测试用例2")
        step_1()
        step_3()


@allure.epic("订单项目")
@allure.feature("支付")
class TestAllureALL2:
    @allure.title("支付成功")
    @allure.story("支付测试用例例1")
    def test_case_1(self, login_fixture):
        print("支付测试用例例1")
        step_3()

    @allure.title("支付失败")
    @allure.story("支付测试用例例2")
    def test_case_2(self, login_fixture):
        print("支付测试用例例2")
        step_4()
