from data_source_txt import DataSourceTxt
__author__ = 'yaoqijun'

if __name__ == '__main__':
    context = {
        'path': 'content.txt'
    }
    source = DataSourceTxt(context)
    data = source.source_data(None)
    print(data)
    print("this input test python content file")