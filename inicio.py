import pymysql.cursors
con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    db="aulapytonfull",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor)


#orm.bold = 'mysql' pode mudar para  sqlite
#orm.bold = 'sqlite'
#orm.criaTabela('minhaTabela')

def criaTabela(nomeTabela):

    try:

       with con.cursor() as cursor:
           cursor.execute(f"create table {nomeTabela} (nome varchar(50))")
       print("tabela criada com sucesso")
    except Exception as e:
       print(f'Ocorreu um erro {e}')

def removeTabela(nomeTabela):

     try:

         with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
         print("tabela removida com sucesso")
     except Exception as e:
         print(f'Ocorreu um erro {e}')


#nome = input('Digite seu nome')
def inserirTabela(nome):
    try:

        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste values ('{nome}')")
        print("Valor inserido com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

try:

    with con.cursor() as cursor:
        cursor.execute("INSERT INTO teste values ('caio')")
    print("Valor inserido com sucesso")
except Exception as e:
    print(f'Ocorreu um erro {e}')


#def selectTabela():
def updateTabela():
 try:

    with con.cursor() as cursor:
        #cursor.execute("SELECT * FROM teste")
        #resultado = cursor.fetchall()
        #print(resultado)
        #print(len(resultado))
        #for i in resultado:
            #print(i)
        #print(len(resultado[0]))

        #Alterar o nome corrigir
         cursor.execute("UPDATE teste SET nome = 'marcos' WERE nome = 'marco'")
    print("Atualização removida com sucesso")
 except Exception as e:
    print(f'Ocorreu um erro {e}')


#x = [{'nome': 'caio', 'id':2}, {'nome': 'marcos', 'id': 3}]


try:

    with con.cursor() as cursor:
        cursor.execute("DELETE FROM teste WHERE nome  = 'caio'")
    print("Remoção efetuada com sucesso")
except Exception as e:
    print(f'Ocorreu um erro {e}')


con.close()