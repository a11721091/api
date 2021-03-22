
class global_var:

    # case_id
    Id = '0'
    url = '1'
    is_run = '2'
    request_way = '3'
    headers = '4'
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    data = '8'
    expect = '9'
    result = '10'


# 获取case_id
def get_id():
    return global_var.Id


# 获取url
def get_url():
    return global_var.url


# 获取是否运行
def get_is_run():
    return global_var.is_run


# 获取请求方式
def get_request_way():
    return global_var.request_way


# 获取请求头
def get_headers():
    return global_var.headers


# 获取请求数据
def get_data():
    return global_var.data


# 获取预期结果
def get_expect():
    return global_var.expect


# 获取实际结果
def get_result():
    return global_var.result
