import xlrd
__author__ = 'yaoqijun'


def read_xls_info():
    book = xlrd.open_workbook("test.xlsx")
    sheet = book.sheets()[0]
    print(sheet.nrows)
    print(sheet.ncols)

if __name__ == '__main__':
    print("this test excel content print")
    read_xls_info()

