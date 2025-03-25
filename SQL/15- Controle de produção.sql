create database Fabrica;
use Fabrica;

create table produtos (
    id serial primary key,
    nome varchar(255) not null,
    descricao text
);

create table producoes (
    id serial primary key,
    produto_id int references produtos(id),
    quantidade int not null,
    data date not null
);

insert into producoes (produto_id, quantidade, data) values (1, 500, '2025-03-15');

select * from producoes where produto_id = 1;

update producoes set quantidade = 600 where id = 1;

delete from producoes where id = 1;