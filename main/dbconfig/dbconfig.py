import pymysql

def conexao():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="catrina",
            autocommit= False,
            connect_timeout=5
        )
        print("\n Conexão concluída.")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if conn is None:
            print("Falha ao estabelecer conexão.")