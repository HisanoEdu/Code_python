create database Gestao;
use Gestao;

create table eventos (
    id serial primary key,
    nome varchar(255) not null,
    data_inicio date not null,
    data_fim date not null,
    local varchar(255) not null
);

create table inscricoes (
    id serial primary key,
    evento_id int references eventos(id),
    participante_id int not null
);

insert into eventos (nome, data_inicio, data_fim, local) values ('conferência tech', '2025-04-10', '2025-04-12', 'centro de convenções');

select * from eventos where '2025-04-10' between data_inicio and data_fim;

update eventos set data_inicio = '2025-04-11', data_fim = '2025-04-13' where id = 1;

delete from inscricoes where id = 1;