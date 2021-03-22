import unittest
from reques import RunMain
from unittest import mock
import json
class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()
    def test_01(self):
        url = 'https://api.ktunes.cn:13001'
        data = {
            "header": {"size": 0, "dst": "", "type": 2, "ver": 512, "lang": "zh_cn", "sess": "83f5892b3f722a5a",
                       "seq": 0,
                       "code": 0, "desc": "", "stmp": 1597219124877, "ext": "CN",
                       "orn": "P1008N19120359$androidPiano$1.0.20$2.3.4$androidFamily", "cmd": "account.login"},
            "body": {"type": 0, "clientType": 3, "userName": 18538313436, "password": "111111"}}
        header = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        mock_data = mock.Mock(return_value=data)
        print(mock_data)
        self.run.runMain = mock_data
        res = self.run.runMain(url, data, 'post', header)
        print(res)
        global userId
        userId = 10090
        print(type(res))
        #self.assertEqual(res['header']['code'], 0, '测试失败')

    def test_02(self):
        print(userId)
        print("test02-start")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_01"))
    unittest.TestRunner().run(suite)