import unittest
from ddt import ddt, data, unpack, file_data
import requests
import xmlrunner
import os
import HtmlTestRunner

path1 = os.path.dirname(os.path.abspath(__file__))
path3 = os.path.join(path1, "uu88.xml")


@ddt
class MyTest01(unittest.TestCase):
    """
    def setUp(self):
        print("do something before test : prepare environment.\n")

    def tearDown(self):
        print("do something after test : clean up.\n")

    @classmethod
    def setUpClass(cls):
        print("this setupclass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        print("this teardownclass() method only called once too.\n")

    """

    # @unpack
    # @data({"url": "http://httpbin.org/post", "method": "POST",
    #        "params_body": "{'key1': 'value1', 'key2': 'value2'}"},
    #       {"url": "http://httpbin.org/get", "method": "GET",
    #        "params_body": "{'key1': 'value1', 'key2': 'value2'}"},
    #       )
    @file_data('data.json')
    def test_case(self, url, method, params_body):
        if method == "POST":
            requests.post(url, json=params_body)
            # a1 = requests.post(url, json=params_body)
            # print(a1.json())
        if method == "GET":
            requests.get(url)
            # a2 = requests.get(url)
            # print(a2.json())

    def test_case01(self):
        self.assertEqual(2, 2)
        print("执行测试用例01")

    def test_case02(self):
        self.assertEqual("2", "2")
        print("执行测试用例02")

    def test_case03(self):
        self.assertNotEqual(2, 3)
        print("执行测试用例03")

    def test_case04(self):
        self.assertIn(2, [2, 3, 4, 5, "a", "b"])
        print("执行测试用例04")


def main():
    with open(path3, 'wb') as e:
        # unittest.main(testRunner=xmlrunner.XMLTestRunner(output=e))
        test_suite = unittest.TestSuite()  # 创建一个测试集合
        # test_suite.addTest(unittest.makeSuite((MyTest5454)))
        test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest01))
        runner = xmlrunner.XMLTestRunner(output=e)
        # runner = HtmlTestRunner.HTMLTestRunner(output=e)
        runner.run(test_suite)
