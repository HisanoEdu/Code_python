create database aluno;
use aluno;

create table Aluno(
Id_aluno int auto_increment primary key,
nome varchar(100) not null,
idade int (30)
);

create table Notas(
Id_notas int auto_increment primary key,
Id_aluno int,
disciplina varchar (100) not null,
nota varchar(10) not null,
foreign key(Id_aluno) references Aluno(Id_aluno)
);

insert into Aluno (Id_aluno,nome,idade) values
(1,"Maria Eduarda Silva", 19),
(2,"Laura Barbosa", 17),
(3,"joão Mendes",18),
(4,"Vitor Santana",19),
(5,"João Vitor da Silva",20);

insert into Notas (Id_aluno,disciplina,nota) values
(1, 'matemática', 8.5),
(1, 'física', 7.0),
(2, 'matemática', 9.0),
(2, 'história', 6.5),
(3, 'física', 7.8),
(4, 'matemática', 6.0),
(5, 'história', 8.2);

select * from Aluno;
select * from Notas;

update Aluno set idade=21  where id_aluno=2; 

delete from Notas where Id_aluno=5;





