create database chamadas;
use chamadas;

create table clientes (
    id serial primary key,
    nome varchar(255) not null
);

create table chamados (
    id serial primary key,
    cliente_id int references clientes(id),
    descricao text not null,
    status varchar(50) check (status in ('aberto', 'resolvido')) default 'aberto'
);

insert into chamados (cliente_id, descricao, status) values (1, 'problema na conexão', 'aberto');

select * from chamados where status = 'aberto';

update chamados set status = 'resolvido' where id = 1;

delete from chamados where id = 1 and status = 'resolvido';