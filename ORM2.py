from sqlalchemy import create_engine, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ORM import Pessoa, session

def RetornaSession(Usuario):
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapytonfull"
    PORTA = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"

    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
   #session = Session()
    return session()

#ession = RetornaSession("root")  # Corrigido para passar o usuário como argumento

   #x = Pessoa(nome='caio',
         # usuario='Marcos',
          #senha='1234')

   #y = Pessoa(usuario='paulo',
         # senha='1234')

 #session.add_all([x, y])
   #session.rollback()

   #session.commit()

## Cria uma nova sessão
  # session = RetornaSession()

# Realiza a consulta na tabela 'Pessoa'
   #x = session.query(Pessoa).all()

# Imprime os resultados da consulta
  # for pessoa in x:
  # print(pessoa)

# Realiza a consulta na tabela 'Pessoa'
   #x = session.query(Pessoa).all()
# Imprime os resultados da consulta
   #for pessoa in x:
   #print(x[0])  printa objeto
   #print(type(x)) para printar list
   #print(type(x[0]))  para acessar clss
   #print(x[0].id) printa ID
   #print(x[0].nome) printa nome
   #print(x[0].usuario) PRINTA USUARIO
  # print(x[0].senha) printa senha
  # print(x[1].id)

  # for i in x:
      # print(i.id)
   #x = session.query(Pessoa).filter_by(usuario='marcos', nome='caio').all()
  # x = session.query(Pessoa).filter_by(usuario='marcos', nome='caio')
   #x = session.query(Pessoa).filter(Pessoa.nome == 'caio')

   #for i in x:
   #print(i.id)
   #print(x)
#codigo em SQL

  # session = RetornaSession()
x = session.query(Pessoa).filter(Pessoa.id == 4).one()
# Realiza a consulta na tabela 'Pessoa' com filtro
  # x = session.query(Pessoa).filter(or_(Pessoa.nome == 'caio', Pessoa.usuario == 'Marcos'))
   #x = session.query(Pessoa).filter(Pessoa.id == 3).all()
    #
# Verifica se há resultados na lista x antes de tentar acessar o primeiro elemento
  # x[0].nome += 'caio'
   #x[0].senha ='novaSenha'

session.delete(x)
session.commit()