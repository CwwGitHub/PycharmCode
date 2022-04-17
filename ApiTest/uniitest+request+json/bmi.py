import unittest
import requests
import json

class bmi_test(unittest.TestCase):
    def  setUp(self):#1、测试固件
        self.url="https://api.jisuapi.com/weight/bmi?"

    def test_succl(self):#2、测试用例：提供基础类testcase,来创建测试用例，test_开头
        params='appkey=cb88aeb5fe3c939a&sex=male&height=175&weight=70'
        r= requests.get(self.url+params)
        data=json.loads(r.text)
        print(data)
        self.assertEqual("正常范围",data["result"]["level"])

    def suite(self):#3、测试套件：决定执行哪些用例
        bmitest = unittest.TestLoader().loadTestsFromTestCase(bmi_test)
        return bmitest

    if __name__=="__main__":#4、测试运行器：执行用例并给出测试结果
        runner=unittest.TextTestRunner()
        runner.run(suite())
