from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except OperationalError as e:
    print(f"The error '{e}' occurred while attempting to connect to the database.")
