from output.source_output import SourceOutputDefault, SourceOutput
__author__ = 'yaoqijun'


def test_condition():
    print("test condition")
    lines = ['123','5123123','42512sadf','sadfasdf','5123423']
    context = {'input_info': lines}
    default = SourceOutputDefault(context)
    print(default.write_out(path='test.txt'))

if __name__ == '__main__':
    test_condition()
