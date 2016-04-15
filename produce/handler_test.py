from handler import Handler
__author__ = 'yaoqijun'


class HandleTest(Handler):
    def handle(self, context):
        context['in handle '] = 'over'


