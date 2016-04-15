__author__ = 'yaoqijun'


def test(*k):
    print(type(list(k)))


def test1():
    l = [1, 2, 3, 4]
    l.pop()
    print(l)

if __name__ == '__main__':
    test1()
