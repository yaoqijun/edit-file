import logging
__author__ = 'yaoqijun'


class SourceOutput(object):
    def __init__(self, context):
        self._context = context

    # write out to file content
    def write_out(self):
        pass

"""
    default text file out put content
"""


class SourceOutputDefault(SourceOutput):
    def __init__(self,context):
        super(SourceOutputDefault, self).__init__(context)

    def write_out(self, **params):
        if not ('path' in params):
            return False
        outputPath = params['path']
        self._write_file(outputPath, self._context['input_info'])

    def _write_file(self, out_path, out_line):
        try:
            f = open(out_path, "w")
            for line in out_line:
                f.write(line+'\n')
            return True
        except RuntimeError as e:
            logging.error("source out put error")
            return False
        finally:
            if f:
                f.close()
