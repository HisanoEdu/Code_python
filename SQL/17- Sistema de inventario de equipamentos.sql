create database equimapamentos;
use equipamentos;

create table equipamentos (
    id serial primary key,
    nome varchar(255) not null,
    quantidade int not null,
    localizacao varchar(255) not null
);

insert into equipamentos (nome, quantidade, localizacao) values ('computador', 10, 'escritório');

select * from equipamentos where quantidade < 5;

update equipamentos set localizacao = 'sala de ti' where id = 1;

delete from equipamentos where id = 1;