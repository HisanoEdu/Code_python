create database funcionario;
use funcionario;

create table funcionarios (
id_funcionario int primary key auto_increment,
nome varchar(100),
cargo varchar(50),
salario varchar(100)
);

insert into funcionarios (id_funcionario,nome, cargo, salario) values
(1,'joão da silva', 'analista de sistemas', 3500.00),
(2,'maria oliveira', 'gerente de marketing', 5500.00),
(3,'pedro santos', 'desenvolvedor', 4000.00),
(4,'ana costa', 'assistente administrativo', 2500.00),
(5,'lucas pereira', 'diretor financeiro', 8000.00);

select nome, cargo, salario
from funcionarios
where salario > 4000;

update funcionarios
set salario = 3800.00
where nome = 'joão da silva';

delete from funcionarios
where nome = 'ana costa';
