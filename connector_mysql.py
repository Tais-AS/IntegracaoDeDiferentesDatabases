import mysql.connector

class interage_mysql:
    usuario, senha, host, banco = "", "", "", ""
    
    def __init__(self, usuario, senha, host, banco):
        
        try:
            self.usuario = usuario
            self.senha = senha
            self.host = host
            self.banco = banco
        except Exception as e:
            print(str(e))

    def conectar(self):
        try:
            con = mysql.connector.connect(user=self.usuario, password=self.senha, host=self.host, database=self.banco)
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print(str(e))


    #metodo para selecionar e gerar a query
    def selecionar(self, query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    def desconectar(self, con, cursor):
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))
        
            

    #def desconectar = conector e cursor
    #metodo para executar a inclusao de dado
    def insert(self, query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            
            return cursor.fetchall()
            #cursor.close()
            #con.commit()
            #con.close()
            
        except Exception as e:
            print("erro insert",str(e))
        finally:
            self.desconectar(con, cursor)

    #funcao para as informacoes necessarias para acesso ao banco de dados
    def get_db_info():
        try:
            user = "root"
            password = "admin"
            host = "127.0.0.1"
            database = "oldtech"
            return user, password, host, database
        except Exception as e:
            print(str(e))

        try:
            con = mysql.connector.connect(user='root', password='admin', host='127.0.0.1', database='oldtech')
            query = "SHOW TABLES"
            cursor = con.cursor()
            cursor.execute(query)
            for row in cursor:
                print(str(row))
            cursor.close()
            con.close()
        except Exception as e:
            print(e)

        

   
        

   
