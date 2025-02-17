import mysql.connector

def concetar():
    return mysql.connector.connect(
        host = "localhost",
        user="root",
        password ="",
        database= "meu_banco"
    )
def adicionar_user(login,senha):
    coenxao = concetar()
    cursor =coenxao.cursor()
    sql = 'INSERT INTO usuqario (email,senha_hash) values (%s , SHA2 (%s,56))'
    valores = (login,senha)
    cursor.close()
    conexao.close()

    