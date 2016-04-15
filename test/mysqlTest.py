import mysql.connector
from input.data_source_mysql import DataSourceMysql
__author__ = 'yaoqijun'


def test_connection():
    print("test connection")
    db = mysql.connector.connect(user='root',password='anywhere',host='127.0.0.1',database='testlink')
    cur=db.cursor()
    cur.execute('select * from Student')
    for row in cur.fetchall():
        print len(row)


def test_data_source_mysql():
    print("test data source mysql connection")
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'testlink',
        'user': 'root',
        'password': 'anywhere',
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
    }
    context = {
        'config': config
    }
    dataSource = DataSourceMysql(context)
    print(dataSource.source_data({'sql': 'select * from Student'}))


if __name__ == '__main__':
    test_data_source_mysql()
