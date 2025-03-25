create database cliente;
use cliente;

create table clientes (
id int primary key auto_increment,
nome varchar(100),
email varchar(100)
);

create table pedidos (
id int primary key auto_increment,
id_cliente int,
dia date,
total decimal(10, 2),
foreign key (id_cliente) references clientes(id_cliente)
);

insert into clientes (nome, email) values
('João Silva', 'joao@email.com'),
('Maria Oliveira', 'maria@email.com'),
('Pedro Santos', 'pedro@email.com');

insert into pedidos (id_cliente, dia, total) values
(1, '2025-03-01', 150.75),
(1, '2025-03-10', 200.50),
(2, '2025-03-02', 300.25),
(3, '2025-03-05', 120.00);



