from urllib.parse import urlparse

from exceptions import InvalidUrlError

import re

def disassemble_url(url):
    regex_mysql_postgree = '^[a-z]+://[a-z]+:[a-z0-9]+@[a-z0-9.]+:[1-9][0-9]*/[a-z]+$'
    regex_sqlite = '^sqlite:///[a-z]+.db$'
    if re.search(regex_mysql_postgree, url) or re.search(regex_sqlite, url):
        url_demount = urlparse(url)
        return url_demount
    else:
        raise InvalidUrlError('URL inválida para o padrão esperado')

def check_connection_type(url_demount):

    connections = {
        'mysql': lambda : create_connection_mysql(url_demount),
        'postgree': lambda : create_connection_postgree(url_demount),
        'sqlite': lambda : create_connection_sqlite(url_demount)
    }

    return connections[url_demount.scheme]()

def create_connection_mysql(connection_data):
    import mysql.connector

    connection = mysql.connector.connect(
        host=connection_data.host,
        user=connection_data.username,
        password=connection_data.password,
        database=connection_data.path.lstrip('/')
    )

    return connection.cursor()

def create_connection_sqlite(connection_data):
    import sqlite3

    connection = sqlite3.connect(connection_data.path)

    return connection.cursor()

def create_connection_postgree(connection_data):
    import psycopg2

    connection = psycopg2.connect(
        host=connection_data.host,
        user=connection_data.username,
        password=connection_data.password,
        database=connection_data.path.lstrip('/'),
        port=connection_data.port
    )

    return connection.cursor()

def create_engine(url):

    url_demount = disassemble_url(url)
    connection = check_connection_type(url_demount)
    
    return connection

if __name__ == '__main__':
     disassemble_url('mysql://bruno:12345@localhost:3366/banco')