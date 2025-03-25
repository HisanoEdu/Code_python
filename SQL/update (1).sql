CREATE DATABASE Cadastro;
USE Cadastro;


CREATE TABLE Estado (
    Id_estado INT PRIMARY KEY AUTO_INCREMENT,
    Estado VARCHAR(50) NOT NULL
);

CREATE TABLE Cidade (
    Id_cidade INT PRIMARY KEY AUTO_INCREMENT,
    Cidade VARCHAR(50) NOT NULL,
    Id_estado INT,
    FOREIGN KEY (Id_estado) REFERENCES Estado(Id_estado)
);

CREATE TABLE Sexo (
    Id_sexo INT PRIMARY KEY AUTO_INCREMENT,
    Sexo VARCHAR(20) NOT NULL
);

CREATE TABLE Nacionalidade (
    Id_nacionalidade INT PRIMARY KEY AUTO_INCREMENT,
    Nacionalidade VARCHAR(50) NOT NULL
);

CREATE TABLE Raca (
    Id_raca INT PRIMARY KEY AUTO_INCREMENT,
    Raca VARCHAR(50) NOT NULL
);

CREATE TABLE Escolaridade (
    Id_escolaridade INT PRIMARY KEY AUTO_INCREMENT,
    Escolaridade VARCHAR(50) NOT NULL
);

CREATE TABLE Estado_Civil (
    Id_estado_civil INT PRIMARY KEY AUTO_INCREMENT,
    Estado_Civil VARCHAR(50) NOT NULL
);

CREATE TABLE Cadastro_Clientes (
    Id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    CPF VARCHAR(14) UNIQUE NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Idade INT NOT NULL,
    RG VARCHAR(12) UNIQUE NOT NULL,
    Id_estado_civil INT,
    Id_cidade INT,
    Id_sexo INT,
    Id_nacionalidade INT,
    Fone VARCHAR(15),
    Id_raca INT,
    Id_escolaridade INT,
    FOREIGN KEY (Id_estado_civil) REFERENCES Estado_Civil(Id_estado_civil),
    FOREIGN KEY (Id_cidade) REFERENCES Cidade(Id_cidade),
    FOREIGN KEY (Id_sexo) REFERENCES Sexo(Id_sexo),
    FOREIGN KEY (Id_nacionalidade) REFERENCES Nacionalidade(Id_nacionalidade),
    FOREIGN KEY (Id_raca) REFERENCES Raca(Id_raca),
    FOREIGN KEY (Id_escolaridade) REFERENCES Escolaridade(Id_escolaridade)
);

UPDATE Cidade 
SET Cidade = CASE 
    WHEN LEFT(Cidade, 1) BETWEEN 'A' AND 'M' THEN 'Abaixo de M'
    ELSE 'Acima de M'
END;

UPDATE Estado 
SET Estado = CASE 
    WHEN Estado IN ('Mato Grosso do Sul', 'Mato Grosso', 'Goiás', 'Distrito Federal') THEN 'Centro Oeste'
    WHEN Estado IN ('São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo') THEN 'Sudeste'
    WHEN Estado IN ('Paraná', 'Santa Catarina', 'Rio Grande do Sul') THEN 'Sul'
    WHEN Estado IN ('Bahia', 'Pernambuco', 'Ceará', 'Alagoas', 'Sergipe', 'Rio Grande do Norte', 'Paraíba', 'Maranhão', 'Piauí') THEN 'Nordeste'
    ELSE 'Norte'
END;

UPDATE Nacionalidade 
SET Nacionalidade = 'Fora do Brasil' 
WHERE Nacionalidade = 'Estrangeiro';

UPDATE Raca 
SET Raca = 'Seres Humanos';

UPDATE Escolaridade 
SET Escolaridade = CASE 
    WHEN Escolaridade IN ('Ensino Fundamental', 'Ensino Médio') THEN 'Ensino Básico'
    WHEN Escolaridade IN ('Graduação', 'Pós-Graduação', 'Mestrado', 'Doutorado') THEN 'Ensino Avançado'
END;

-- Selects conforme solicitado
SELECT Nome, Cidade FROM Cadastro_Clientes
JOIN Cidade ON Cadastro_Clientes.Id_cidade = Cidade.Id_cidade;

SELECT Nome, Estado FROM Cadastro_Clientes
JOIN Estado ON Cadastro_Clientes.Id_estado = Estado.Id_estado;

SELECT Nome, CPF, Raca FROM Cadastro_Clientes
JOIN Raca ON Cadastro_Clientes.Id_raca = Raca.Id_raca;

SELECT Nome, Nacionalidade FROM Cadastro_Clientes
JOIN Nacionalidade ON Cadastro_Clientes.Id_nacionalidade = Nacionalidade.Id_nacionalidade;

SELECT Nome, Escolaridade FROM Cadastro_Clientes
JOIN Escolaridade ON Cadastro_Clientes.Id_escolaridade = Escolaridade.Id_escolaridade;

SELECT Nome, Cidade, Estado FROM Cadastro_Clientes
JOIN Cidade ON Cadastro_Clientes.Id_cidade = Cidade.Id_cidade
JOIN Estado ON Cadastro_Clientes.Id_estado = Estado.Id_estado;

SELECT Nome, Cidade, Estado, Fone, RG, Sexo, Nacionalidade, Raca, Escolaridade FROM Cadastro_Clientes
JOIN Cidade ON Cadastro_Clientes.Id_cidade = Cidade.Id_cidade
JOIN Estado ON Cadastro_Clientes.Id_estado = Estado.Id_estado
JOIN Sexo ON Cadastro_Clientes.Id_sexo = Sexo.Id_sexo
JOIN Nacionalidade ON Cadastro_Clientes.Id_nacionalidade = Nacionalidade.Id_nacionalidade
JOIN Raca ON Cadastro_Clientes.Id_raca = Raca.Id_raca
JOIN Escolaridade ON Cadastro_Clientes.Id_escolaridade = Escolaridade.Id_escolaridade;
