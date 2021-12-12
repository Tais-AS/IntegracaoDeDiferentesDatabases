from cassandra.cluster import Cluster
from cassandra.cluster import uuid

# apresentar menu: trabalhar martriz ou filial?


# Etapa A popular bancos mysql e cassandra
    # criar os bancos
    # tratamento de dados ...
# Etapa B buscar dados no mysql e colocar no cassandra
    # fazer um select no banco mysql vários de uma vez
    # fazer insert no banco cassandra
# Etapa C mostra os views no banco cassandra
#   com todos os 2 mil registros


class interage_cassandra:
    ##  TODO:
    
    # Criar métodos para criar views
    # tornar o delete mais confiável sem precisar ver a chave primária
    # mudar update e delete para ser geral como fazer para saber qual 
    
    database = ""
    tabela = ""
    session = ""
    
    def __init__(self, database, tabela):
        self.set_database(database)
        self.set_tabela(tabela)
        
        clstr = Cluster()    
        self.session=clstr.connect(self.database) 
    
    #   Setters              
    def set_database(self, database='soulcode'):
        self.database = database
          
    def set_tabela(self, tabela):
        self.tabela = tabela
    
    #   Getters
    
    def get_database(self):
        return self.database
          
    def get_tabela(self):
        return self.tabela
    
      
    def insert(self, values):
        
        self.session.execute(
        f"""
        INSERT INTO {self.tabela} (nota_fiscal, vendedor, total, id_vendas)
        VALUES (%s, %s, %s, %s)
        """,
        (values[0], values[1], values[2], uuid.uuid1())
        )

    
    def select(self,query): 
        
        dados = self.session.execute(query)

        return dados
        
    def update(self):#Todo
        #   ,muda_coluna,coluna_pesquisa,entry_where, new_value
        
        nome_tabela=self.tabela
        query_select=f"Select * from {nome_tabela} limit 10;"
        conjunto_colunas=self.select(query_select)
        
        for linha in conjunto_colunas:
            
            print(linha.id_vendas)

    def delete(self): #Todo
        query = "DELETE FROM alunos WHERE matricula = 390faf8c-1471-446f-9bba-4ee97a3ebc39"
        # Remove o registro
        self.session.execute(query)
        print(query)       
        

# fontes

#https://docs.datastax.com/en/developer/python-driver/3.21/getting_started/
