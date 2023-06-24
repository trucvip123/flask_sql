import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sql-db-server-trucnv.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'sql-database-trucnv'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'trucnv'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Lumia930@'
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '??charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
