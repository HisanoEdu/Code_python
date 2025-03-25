create database Cidadao;
use Cidadao;

create table estado(
id_estado int auto_increment primary key,
nome varchar(100) not null,
uf char(2) not null
);

create table cidade(
id_cidade int auto_increment primary key,
nome varchar(100) not null,
id_estado int,
foreign key (id_estado) references estado(id_estado)
); 

create table genero (
id_genero int primary key auto_increment,
descricao varchar(50) not null
);

create table raca(
id_raca int primary key auto_increment,
descricao varchar(50) not null
);

create table religiao(
id_religiao int primary key auto_increment,
descricao varchar(50) not null
);

create table agencias (
id_agencia int primary key auto_increment,
numero_agencia varchar(10) not null,
endereco varchar(200) not null,
id_cidade int,
foreign key (id_cidade) references cidade(id_cidade)
);

create table clientes (
    id_cliente int primary key auto_increment,
    numero_conta varchar(20) not null unique,
    nome varchar(100) not null,
    cpf varchar(11) not null unique,
    id_cidade int,
    id_estado int,
    id_genero int,
    id_raca int,
    id_religiao int,
    id_agencia int,
    saldo decimal(15,2) default 0.00,
    foreign key (id_cidade) references cidade(id_cidade),
    foreign key (id_estado) references estado(id_estado),
    foreign key (id_genero) references genero(id_genero),
    foreign key (id_raca) references raca(id_raca),
    foreign key (id_religiao) references religiao(id_religiao),
    foreign key (id_agencia) references agencias(id_agencia)
    );
    
    create table saque (
    id_operacao int primary key auto_increment,
    id_agencia int,
    id_cliente int,
    valor decimal(15,2) not null,
    data_operacao datetime default current_timestamp,
    foreign key (id_agencia) references agencias(id_agencia),
    foreign key (id_cliente) references clientes(id_cliente)
    );
    
   create table deposito (
    id_operacao int primary key auto_increment,
    id_agencia int,
    id_cliente int,
    valor decimal(15,2) not null,
    data_operacao datetime default current_timestamp,
    foreign key (id_agencia) references agencias(id_agencia),
    foreign key (id_cliente) references clientes(id_cliente)
    );
    
    
delimiter $
create trigger trg_saque_saldo_deposito
before insert on saque
for each row
begin
update cliente
set saldo = new.id_cliente;
end$;
delimiter ;
    
delimiter $
create trigger trg_atualiza_saldo_deposito
before insert on deposito
for each row
begin
update cliente
set saldo = new.id_valor;
end$;
delimiter ;