import logging
__author__ = 'yaoqijun'


"""
    execute handle executor
"""


class HandleExecutor(object):
    def __init__(self, chain):
        if not isinstance(chain, HandlerChain):
            logging.error("init error input type not an chain type")
        else:
            self._chain = chain

    def execute(self, context):
        handle_list = self._chain.gain_handler()
        try:
            for handle in handle_list:
                handle.handle(context)
            return True
        except RuntimeError as e:
            logging.error('catch hangle execute error', e)
            return False



"""
    handle chain
"""


class HandlerChain(object):
    def __init__(self, *kt):
        self._handle_list = list(kt)

    def add_handle(self, h):
        self._handle_list.append(h)

    def clear_handle(self):
        self._handle_list = []

    def remove_handle(self, x):
        self._handle_list.remove(x)

    def gain_handler(self):
        return self._handle_list


"""
    handle deal Context Data content
"""


class Handler(object):
    # handle context
    def handle(self, context):
        pass

