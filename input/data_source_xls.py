from data_source import DataSource
import xlrd
import logging
__author__ = 'yaoqijun'


"""
    excel data source info import
"""


class DataSourceXls(DataSource):
    def __init__(self, context):
        super(DataSourceXls, self).__init__(context)

    """
        :param{sheetNumber: default first page, rows : default max rows , cols default max cols}
    """
    def source_data(self, **params):
        source = excel_source(self._source_context['path'])
        data = {}
        input_info = []
        context = []
        # TODO shit 


def excel_source(path):
    try:
        data = xlrd.open_workbook(path)
        return data
    except IOError as e:
        logging.error("error get excel data")
