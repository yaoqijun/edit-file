from source_output import SourceOutputTxt
__author__ = 'yaoqijun'

"""
    default data source output info
"""


class DefaultSourceOutput(object):
    def __init__(self, path):
        self._path = path
        self._source = SourceOutputTxt(None)

    def write_out(self):
        self._source.write_out(path=self._path)

