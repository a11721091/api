import json
#fp = open("../config/login.json")
#data = json.load(fp)
#print(data['login'])
class OpertionJson:
    def __init__(self, json_name=None):
        if json_name:
            self.json_name = json_name
        else:
            self.json_name = "../config/login.json"
        self.data = self.read_data()

    def read_data(self):
        with open(self.json_name) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self, name):
        return self.data[name]


if __name__ == '__main__':
    opers = OpertionJson()
    print(opers.get_data('login'))