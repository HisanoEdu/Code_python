create database Bibliotecas;
use Bibliotecas;

create table livros (
    id int primary key,
    nome varchar(255),
    autor varchar(255)
);

create table emprestimos (
    id int primary key,
    livro_id int,
    usuario_id int,
    data_emprestimo date,
    data_devolucao date,
    foreign key (livro_id) references livros(id)
);

insert into livros (id, nome, autor)
values (1, '1984', 'george orwell'),
       (2, 'o senhor dos anéis', 'j.r.r. tolkien');

insert into emprestimos (id, livro_id, usuario_id, data_emprestimo, data_devolucao)
values (1, 1, 101, '2025-03-15', '2025-03-22'),
       (2, 2, 102, '2025-03-14', '2025-03-21');

select * from livros;

select * from emprestimos;

update emprestimos
set data_devolucao = '2025-03-25'
where id = 1;

delete from emprestimos
where id = 2;

