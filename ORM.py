from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "aulapytonfull"
PORTA = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

Base.metadata.create_all(engine)

#print(type(Session))
#print(type(Session))

#print("class \"sql1chemy.orm.session.sessionmaker>")