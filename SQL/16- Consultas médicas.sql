create database Consultas;
use Consultas;

create table consultas (
    id serial primary key,
    paciente_id int not null,
    medico_id int not null,
    data date not null,
    horario time not null
);

insert into consultas (paciente_id, medico_id, data, horario) values (1, 1, '2025-03-16', '14:00');

select * from consultas where medico_id = 1 and data = '2025-03-16';

update consultas set horario = '15:00' where id = 1;

delete from consultas where id = 1;