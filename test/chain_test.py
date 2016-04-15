from produce.handler import HandlerChain,Handler,HandleExecutor
from produce.handler_test import HandleTest
__author__ = 'yaoqijun'


def main_condition():
    print("test main condition")
    chain = HandlerChain(HandleTest())
    context = {}
    executor = HandleExecutor(chain)
    executor.execute(context)
    print(context)

if __name__ == '__main__':
    main_condition()
