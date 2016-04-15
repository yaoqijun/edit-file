import xlrd
from input.data_source_xls import DataSourceXls
__author__ = 'yaoqijun'


def test_fun():
    print("test function content")
    context = {
        'path': 'test.xlsx',
        'index': 3,
        'startRow': 10,
        'endRow': 20,
        'startCol': 4,
        'endCol': 10
    }
    source = DataSourceXls(context)
    data = source.source_data(sheetIndex=3, startRow=10, endRow=20, startCol=4, endCol=10)
    print(data)


if __name__ == '__main__':
    test_fun()
