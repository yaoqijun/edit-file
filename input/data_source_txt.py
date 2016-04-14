from data_source import DataSource
import logging

__author__ = 'yaoqijun'


# this is txt data source
class DataSourceTxt(DataSource):
    """
        context source
    """
    def __init__(self, context):
        super(DataSourceTxt, self).__init__(context)

    """
      get path info content
    """
    def source_data(self, params):
        path = self._source_context['path']
        # build data context
        data = {}
        input_info = []
        context = {}
        try:
            i = 0
            f = open(path,'r')
            for line in f.readlines():
                input_info.append(line.strip())
                i += 1
            data['input_info'] = input_info
            context['has_data'] = True
            context['total_line'] = i
        except IOError as e:
            logging.error("data source input error, file text info")
            context['has_data'] = False
            context['total_line'] = 0
        finally:
            if f:
                f.close()
            context['type'] = 'txt'
            data['context'] = context
        return data


