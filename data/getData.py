from util.operationExcel import OperationExcel
import data.dataConfig
from util.opertionJson import OpertionJson


class GetData:
    def __init__(self):
        self.operation_excel = OperationExcel()

    # 获取excel行数
    def get_case_lines(self):
        return self.operation_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = data.dataConfig.get_is_run()
        run_model = self.operation_excel.get_cell_value(row, col)
        if run_model == 'yes':
            return flag == True
        else:
            return flag == False

    # 是否携带header
    def is_header(self, row):
        col = data.dataConfig.get_headers()
        header = self.operation_excel.get_cell_value(row, col)
        if header == 'yes':
            return 'header'
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = data.dataConfig.get_request_way()
        request_method = self.operation_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_url(self, row):
        col = data.dataConfig.get_url()
        url = self.operation_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = data.dataConfig.get_data()
        request_data = self.operation_excel.get_cell_value(row, col)
        if request_data == '':
            return None
        return request_data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OpertionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = data.dataConfig.get_expect()
        expect = self.operation_excel.get_cell_value(row, col)
        return expect

