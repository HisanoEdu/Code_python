create database Venda;
use Venda;

create table item_venda(
venda int primary key,
produto varchar(3),
quantidade int,
foreign key (produto) references produto (referencial));

insert into item_venda values (1,'001',3);
insert into item_venda values (2,'002',1);
insert into item_venda values (2,'003',5);

select * from venda;