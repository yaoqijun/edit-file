__author__ = 'yaoqijun'


# data source user definition different source
class DataSource(object):
    """
        context text info
        example : file path, type   source con info
    """
    def __init__(self, context):
        self._source_context = context

    """
        :param get info
    """
    def source_data(self, params):
        pass
