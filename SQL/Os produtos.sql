create database Produto;
use Produto;

create table produto(
referencia varchar(3) primary key,
descricao varchar(50) unique,
estoque int not null default 0);

insert into produto values ('001', 'Feijão', 10);
insert into produto values ('002', 'Arroz' ,5);
insert into produto values ('003', 'Farinha',15);

select * from produto;