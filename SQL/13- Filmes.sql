create database Filmes;
use Filmes; 

create table filmes (
id serial primary key,
nome varchar(255) not null,
duracao int not null,
classificacao varchar(20) not null
);

create table salas (
id serial primary key,
nome varchar(100) not null,
capacidade int not null
);

insert into filmes (nome, duracao, classificacao) values ('inception', 148, '14 anos');
insert into salas (nome, capacidade) values ('sala 1', 100);

select filmes.* from filmes
join salas on salas.id = filmes.id
where salas.nome = 'sala 1';

update filmes set classificacao = '12 anos' where id = 1;

delete from filmes where id = 1;