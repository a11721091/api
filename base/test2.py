data= {'header': {'type': 18, 'cmd': 'account.login', 'ver': 512, 'lang': 'zh-CN', 'code': 0, 'desc': '成功', 'stmp': 1598945472402}, 'body': {'name': 18538313436, 'sess': 'd58cb39d92f6674c', 'userId': 16090, 'mark': 172, 'userType': 1}}

desc = data['header']['desc']
print(type(data))
print(desc)
