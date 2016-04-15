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
        book = excel_source(self._source_context['path'])
        input_info = []
        context = {}

        """
            get user definition excel info
        """
        sheetIndex = 0
        if "sheetIndex" in params:
            sheetIndex = params['sheetIndex'] - 1

        sheet = book.sheet_by_index(sheetIndex)

        startRow = 0
        if 'startRow' in params:
            startRow = params['startRow'] - 1

        endRow = sheet.nrows - 1
        if 'endRow' in params:
            endRow = params['endRow'] - 1

        startCol = 0
        if 'startCol' in params:
            startCol = params['startCol'] - 1

        endCol = sheet.ncols - 1
        if 'endCol' in params:
            endCol = params['endCol'] - 1

        try:
            """
                read data form sheet
            """

            for i in range(startRow, endRow + 1):
                row_data = []
                row = sheet.row_values(i)
                for j in range(startCol, endCol + 1):
                    row_data.append(row[j])
                input_info.append(row_data)

            context['has_data'] = True
            context['total_line'] = endRow - startRow + 1
        except IOError as e:
            logging.error("io input exception")
            context['has_data'] = False
            context['total_line'] = 0
        finally:
            context['type'] = 'xlsx'

        data = {
            'input_info': input_info,
            'context': context
        }
        return data


def excel_source(path):
    try:
        data = xlrd.open_workbook(path)
        return data
    except IOError as e:
        logging.error("error get excel data")
