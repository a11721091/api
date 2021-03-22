from unittest import mock
import xlrd

def mock_test(mock_methhod, request_data, url, method, response_data):
    mock_methhod = mock.Mock(return_value=response_data)