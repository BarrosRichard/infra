from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import json

load_dotenv() # carrega as váriaveis contidas em .env
CONFIG_DB = json.loads(os.getenv('CONFIG_DB')) # requisita a váriavel em string e converte para json

class Database(): # contem informações importantes para conexão e manípulação do banco
    def __init__(self):
        self.engine = create_engine(f'mysql+pymysql://{CONFIG_DB["username"]}:{CONFIG_DB["password"]}@{CONFIG_DB["host"]}:{CONFIG_DB["port"]}/{CONFIG_DB["database"]}') # engine de conexão
        self.base = declarative_base() # base para criar modelos
        self.Session = sessionmaker(bind=self.engine) # sessão para execução de querys