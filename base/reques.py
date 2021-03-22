import requests
import json


class RunMain:

 #   def __init__(self, url, data, method, header):
 #       self.res = self.runMain(url, data, method, header)

    def sendPost(self,url, data, header):
        res = requests.post(url=url, data=data, headers=header).json()
        return res

    def sendGet(self,url, data, header):
        res = requests.get(url=url, data=data, headers=header).json()
        return res

    def runMain(self,url, data, method, header):
        data = json.dumps(data)
        if method == 'GET' or method == 'get':
            res = self.sendGet(url, data, header)
        else:
            res = self.sendPost(url, data, header)
        return json.dumps(res, indent=2,sort_keys=True)



if __name__ == '__main__':
    url = 'https://api.ktunes.cn:13001'
    data = {
        "header": {"size": 0, "dst": "", "type": 2, "ver": 512, "lang": "zh_cn", "sess": "83f5892b3f722a5a", "seq": 0,
                   "code": 0, "desc": "", "stmp": 1597219124877, "ext": "CN",
                   "orn": "P1008N19120359$androidPiano$1.0.20$2.3.4$androidFamily", "cmd": "account.login"},
        "body": {"type": 0, "clientType": 3, "userName": 18538313436, "password": "111111"}}
    header = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    #data = json.dumps(data)
    run = RunMain().runMain(url, data, 'post', header)
    print(run)



