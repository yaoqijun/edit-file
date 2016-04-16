__author__ = 'yaoqijun'


"""
    definition function to convert string context
"""
a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')
convert = a - A


def to_sub_model(content):
    s = ''
    length = len(content)
    if length == 0:
        return s

    for c in content:
        index = ord(c)
        if Z >= index >= A:
            s = s + '_' + chr(index + convert)
        else:
            s = s + c
    return s


def replace_sub_mode(content):
    s = ''
    i = 0
    while i < len(content):
        c = content[i]
        if c == '_':
            s += chr(ord(content[i+1]) - convert)
            i += 2
        else:
            s += c
            i += 1
    return s
