from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

conf_db = {'host' : 'mysql741.umbler.com',
            'port' : 41890,
            'username' : 'dataflow-user-db',
            'password' : '*Rcf7qt#5VFE',
            'database' : 'dataflow',}

class Database():
    def __init__(self):
        self.engine = create_engine(f'mysql+pymysql://{conf_db["username"]}:{conf_db["password"]}@{conf_db["host"]}:{conf_db["port"]}/{conf_db["database"]}')
        self.base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.infra = self.Session()