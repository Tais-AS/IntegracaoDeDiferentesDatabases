create database if not exists oldtech;

-- use oldtech
create table if not exists sistemaa (
id_vendas int(10)auto_increment, 
nota_fiscal int(10),
vendedor varchar(30),
total float,
primary key (id_vendas)

);
