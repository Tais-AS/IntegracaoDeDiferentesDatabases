# **Integração de diferentes databases via Python**
  
 #### **Desenvolvido por:**  

- [Edson Sabino da Silva](https://github.com/edsonkoreano)
- [Patriccia Àvila](https://github.com/patricciaavila)
- [Tais de Assis Santos](https://github.com/Tais-AS)

#### **Proposta:**

Este é um repositório referente a uma atividade em grupo do curso do Eng. Dados+Python Turma BC8 - SoulCode Academy.

**O que deve ser feito:**

O objetivo é desenvolver  um código em Python que leia a db SQL, corrija, padronize e insira os dados na db noSQL.

**Anexos:**

- [Sistema A](Sistema_A_SQL.csv)
- [Sistema B](Sistema_B_NoSQL.csv)

#### **Requisitos Obrigatórios**

- Os códigos desenvolvidos
- Cronograma apresentando quem fez o que e quando
- Resolução do Projeto


| 🛠️ Tecnologias utilizadas || 
| --- | --- |
|Python
|Visual Studio Code
|Meet
|MySQL
|Cassandra
|Metodologia Ageis  - Projects Git |
|  |

# Resolução

### **1º Criar o banco de dados**

  ####   ✅ [Dados da DB  SQL - MySQL](banco_sql_sistemaa.sql)

    - id_vendas: autogerado e chave primária
    - nota_fiscal: inteiro (10) 
    - vendedor: texto (30) 
    - Total: float


   ####   ✅ [Dados da DB NoSQL - Cassandra](banco_cassandra.sql)

    - id_vendas:identificador único universal e chave primária
    - nota_fiscal: inteiro
    - vendedor: texto  
    - Total: float

### **2º Inserção no bancos**

- [Tratamento do dados](popularBancos.py)

### **3º Connectores**

- [MySQL](connector_mysql.py)
- [Cassandra](connector_cassandra.py)



# **Orientadores**

[Prof Adriano Gomes](https://www.linkedin.com/in/adriannogs/)  
[Prof Felipe Barroso](https://www.linkedin.com/in/felipe-soares-muylaert-barroso-1a603a116/://www.linkedin.com/in/adrianhttps://www.linkedin.com/in/felipe-soares-muylaert-barroso-1a603a116/)

