import mysql.connector
from data_source import DataSource
import logging
__author__ = 'yaoqijun'


class DataSourceMysql(DataSource):
    def __init__(self, context):
        super(DataSourceMysql, self).__init__(context)
        if 'config' in context:
            self._config = context['config']
        else:
            logging.error("data source mysql import error")

    """
        :params contain sql param , to point data source sql info
    """
    def source_data(self, params):
        if not ('sql' in params):
            logging.error("mysql param query error, no sql")
            return

        sql = params['sql']
        input_info = []
        context = {}

        conx = mysql.connector.connect(**self._config)
        try:
            cur = conx.cursor()
            cur.execute(sql)

            """
                row number connector test
            """
            row_number = 0
            for row in cur.fetchall():
                input_info.append(row)
                row_number += 1
            cur.close()

            context['has_data'] = True
            context['total_lines'] = row_number
        except RuntimeError as e:
            logging.error("fail to load data from mysql data source")
            context['has_data'] = False
            context['total_lines'] = 0
        finally:
            if conx:
                conx.close()
            context['type'] = 'mysql'

        return {'input_info': input_info, 'context': context}
