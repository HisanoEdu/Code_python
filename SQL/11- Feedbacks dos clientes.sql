create database Feedbacks;
use Feedbacks;

create table feedbacks (
    id serial primary key,
    cliente_id int not null,
    data date not null,
    comentario text
);

insert into feedbacks (cliente_id, data, comentario) values (1, '2025-03-15', 'ótimo serviço!');

select * from feedbacks where data between '2025-03-01' and '2025-03-15';

update feedbacks set comentario = comentario || ' | resposta: agradecemos pelo feedback!' where id = 1;

delete from feedbacks where id = 1;