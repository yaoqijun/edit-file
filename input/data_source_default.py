from data_source_txt import DataSourceTxt
__author__ = 'yaoqijun'


class DefaultDataReader(object):
    def __init__(self, path):
        context = {
            'path': path
        }
        self._source = DataSourceTxt(context)

    """
        read data from data source
    """
    def read_data(self):
        return self._source.source_data(None)
