create database estoque;
use estoque;


create table produtos (
id_produtos int primary key auto_increment,
nome varchar(100),
quantidade int,
preco varchar(50)
);

insert into produtos (nome, quantidade, preco) values
('produto a', 100, 25.50),
('produto b', 50, 10.00),
('produto c', 20, 15.75),
('produto d', 5, 40.00),
('produto e', 200, 5.99);

select nome, quantidade, preco
from produtos
where quantidade < 20;

update produtos
set quantidade = quantidade - 3
where nome = 'produto b';

delete from produtos
where nome = 'produto d';
