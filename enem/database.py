#Este arquivo possui todas as funções referentes a conexao e utilização
#do banco de dados mysql com python! 
#Iremos criar uma "receita de bolo" para usarmos nos softwares que criarmos!
#Depois de criado , voce tera que importar esse arquivo no programa que quiser
#usar o banco
#Será possivel realizar todas operações CRUD! 
#CRUD = CREATE READ UPDATE DELETE 

import mysql.connector
from mysql.connector import Error

#Configurações padrão do banco

HOST="localhost" #ip da maquina
USER="root" #usuario do banco mysql
PASSWORD="root" #senha do banco mysql
DATABASE="enem" #banco que irá conectar (criar o banco primeiro)

def config(banco):
    #Usar essa função sempre no começo de um novo projeto
    #para apontar qual banco ela vai se conectar
    global DATABASE
    DATABASE = banco

def abrir_conexao():
    #Abre e retorna a conexao com o banco mysql
    try:
        conexao = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE)
        
        if conexao.is_connected():
           return conexao
       
    except Error as e:
        print(f"Erro: {e}")


def fechar_conexao(conexao,cursor):
    #Fecha a conexao e o cursor com segurança! 
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        

def execute_non_query(sql):
    #Essa funcao executa todos comandos sql exceto o select , por isso chama "non query"
    # ou seja, sem consulta ou sem select!
    try:
        conexao = abrir_conexao()
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.execute(sql) #Executa o sql porem não salva efetivamente no banco
            conexao.commit() #Confirma a alteração no banco
        
    except Error as e:
        print(f"Erro na funcao nonquery: {e}")
    
    finally:
        fechar_conexao(conexao,cursor)



def execute_query(sql):
    #Essa funcao executa apenas comandos query , ou seja, select! 
    try:
        conexao = abrir_conexao()
        
        if conexao.is_connected():
            #o parametro dictionary = true permite ler as colunas do banco pelo nome
            #sem esse parametro só é possivel ler pelo indice
            
            cursor = conexao.cursor(dictionary=True) 
            cursor.execute(sql) #Executa o sql select
            dados = cursor.fetchall() #Retorna os dados como dicionario
    
            return dados
        
    except Error as e:
        print(f"Erro na funcao query: {e}")
    finally:
        fechar_conexao(conexao,cursor)