import sqlite3

CAMINHOBANCO=""

def config(banco):
    global CAMINHOBANCO
    CAMINHOBANCO=banco

def Open():
    #Abre a conexão com o banco 
    #Cria o arquivo do banco de dados 

    conexão = sqlite3.connect(CAMINHOBANCO)
    #O código abaixo permite ler as colunas do banco pelo nome!
    conexão.row_factory = sqlite3.Row
    return conexão

#Função para executar (UPDATE,DELETE,INSERT,ETC...)
#Tudo menos SELECT!
def execute_non_query(sql):
    con = Open()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

#Função para executar query(consulta comando SELECT)
def execute_query(sql):
    con = Open()
    cursor = con.cursor()
    cursor.execute(sql)
    return cursor.fetchall()





