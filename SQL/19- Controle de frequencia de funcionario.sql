create database Funcionario;
use Funcionario;

create table funcionarios (
id serial primary key,
nome varchar(255) not null,
cargo varchar(255) not null
);

create table frequencias (
    id serial primary key,
    funcionario_id int references funcionarios(id),
    data date not null,
    hora_entrada time not null,
    hora_saida time
);

insert into frequencias (funcionario_id, data, hora_entrada) values (1, '2025-03-15', '08:00');

select * from frequencias where funcionario_id = 1 and hora_entrada is null;

update frequencias set hora_saida = '17:00' where id = 1;

delete from frequencias where id = 1;