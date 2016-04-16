from handler import Handler
__author__ = 'yaoqijun'


class HandlerEachLine(Handler):
    def __init__(self, function_list):
        self._function_list = function_list

    """
        context input_data handle info
    """
    def handle(self, context):
        if 'input_info' not in context:
            return False
        input_info = context['input_info']
        for fun in self._function_list:
            input_info = map(fun, input_info)
        context['input_info'] = input_info
        return True


def build_function_list(*l):
    return list(l)

