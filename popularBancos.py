

from modules.conector_cassandra import interage_cassandra
from modules.conector_mysql import interage_mysql
import pandas as pd


# --   Para cassandra
    
    database = 'oldtech'
    nome_tabela = 'sistemab'
    df_cassandra = pd.read_csv("Sistema_B_NoSQL.csv", sep=",")    
    df_cassandra.fillna('', inplace=True)   # Colocar valor padrão no nan
    lista_cassandra=df_cassandra.values.tolist()
    obj_cassandra = interage_cassandra(database,nome_tabela)
    
    for linha in lista_cassandra:
        try:
            tup_valores=(linha[0], linha[1], linha[2])
            obj_cassandra.insert(tup_valores)
            
        except Exception as e:
            print("erro",str(e))
            
    # --   Para Mysql
    
    df_mysql=pd.read_csv("Sistema_A_SQL.csv", sep=",")
    df_mysql.fillna('', inplace=True) # Colocar valor padrão no nan
    obj_mysql=interage_mysql("root","#Es181192","localhost","oldtech")
    lista_mysql=df_mysql.values.tolist()

    for linha in lista_mysql:#lista_df_unico:
        try:
            tup_valores=(linha[0], linha[1], linha[2])
            query="INSERT INTO sistemaa (nota_fiscal,vendedor,total) VALUES ('%d', '%s', '%f');" % tup_valores
            obj_mysql.insert(query)
            
        except Exception as e:
            print("erro",str(e))
    
    
    
   
    
    
