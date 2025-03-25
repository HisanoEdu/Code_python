create database Contas;
use Contas;

create table contas (
    id serial primary key,
    descricao varchar(255) not null,
    valor decimal(10,2) not null,
    data_vencimento date not null,
    tipo varchar(50) check (tipo in ('pagar', 'receber'))
);

insert into contas (descricao, valor, data_vencimento, tipo) values ('aluguel', 1500.00, '2025-03-20', 'pagar');

select * from contas where extract(month from data_vencimento) = 3;

update contas set data_vencimento = '2025-03-25' where id = 1;

delete from contas where id = 1;