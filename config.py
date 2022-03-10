from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import json

load_dotenv()
CONFIG_DB = json.loads(os.getenv('CONFIG_DB'))

class Database():
    def __init__(self):
        self.engine = create_engine(f'mysql+pymysql://{CONFIG_DB["username"]}:{CONFIG_DB["password"]}@{CONFIG_DB["host"]}:{CONFIG_DB["port"]}/{CONFIG_DB["database"]}')
        self.base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.infra = self.Session()