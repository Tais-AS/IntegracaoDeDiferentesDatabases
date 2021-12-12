CREATE KEYSPACE IF NOT EXISTS oldtech
WITH replication = {'class' : 'SimpleStrategy', 'replication_factor': 1};
-------------------------------------------------------------------------------
use oldtech;
-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS "oldtech"."sistemab"(
id_vendas uuid PRIMARY KEY, 
nota_fiscal int,
vendedor text,
total float,
);
