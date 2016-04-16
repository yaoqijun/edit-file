from produce.handler_each_line import build_function_list,HandlerEachLine
__author__ = 'yaoqijun'


def test(*k):
    print(type(list(k)))


def test1():
    l = [1, 2, 3, 4]
    l.pop()
    print(l)


def test_build_function():
    l = [1, 2, 3, 4]
    fun_list = build_function_list(lambda x: x+1, lambda x: x * 10)
    print map(fun_list[0], map(fun_list[1], l))


def handle_each_line_test():
    l = [1, 2, 3, 4]
    handler = HandlerEachLine(build_function_list(lambda x: x+1, lambda x: x*10))
    context = {
        'input_info': l
    }
    handler.handle(context)
    print context


def test_str_content():
    s = 'yaoqijun'
    print(len(s))
    print(s[0])

if __name__ == '__main__':
    test_str_content()
