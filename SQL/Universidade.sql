create database universidade;
use universidade;

CREATE TABLE DEPARTAMENTO (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    codigo VARCHAR(10) NOT NULL,
    telefone VARCHAR(20),
    centro VARCHAR(50)
);

CREATE TABLE CURSO (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('Técnico', 'Graduação', 'Mestrado', 'Doutorado') NOT NULL,
    id_departamento INT,
    coordenador VARCHAR(100),
    vice_coordenador VARCHAR(100),
    FOREIGN KEY (id_departamento) REFERENCES DEPARTAMENTO(id_departamento)
);

CREATE TABLE ALUNO (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    numero_matricula VARCHAR(20) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    endereco_rua VARCHAR(100),
    endereco_cidade VARCHAR(50),
    endereco_cep VARCHAR(10),
    telefone VARCHAR(100),
    data_nascimento DATE,
    sexo CHAR(1),
    id_departamento INT,
    id_curso INT,
    FOREIGN KEY (id_departamento) REFERENCES DEPARTAMENTO(id_departamento),
    FOREIGN KEY (id_curso) REFERENCES CURSO(id_curso)
);

CREATE TABLE PROFESSOR (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    id_departamento INT,
    telefone VARCHAR(20),
    FOREIGN KEY (id_departamento) REFERENCES DEPARTAMENTO(id_departamento)
);

CREATE TABLE DISCIPLINA (
    id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    codigo VARCHAR(20) NOT NULL,
    numero_creditos INT NOT NULL,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES DEPARTAMENTO(id_departamento)
);

CREATE TABLE OFERTA_DISCIPLINA (
    id_oferta INT AUTO_INCREMENT PRIMARY KEY,
    id_professor INT,
    id_disciplina INT,
    horario VARCHAR(50),
    FOREIGN KEY (id_professor) REFERENCES PROFESSOR(id_professor),
    FOREIGN KEY (id_disciplina) REFERENCES DISCIPLINA(id_disciplina)
);

CREATE TABLE MATRICULA (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    id_oferta INT,
    FOREIGN KEY (id_aluno) REFERENCES ALUNO(id_aluno),
    FOREIGN KEY (id_oferta) REFERENCES OFERTA_DISCIPLINA(id_oferta)
);

INSERT INTO DEPARTAMENTO (nome, codigo, telefone, centro) VALUES
('Departamento de Computação', 'D001', '123456789', 'Centro de Ciências'),
('Departamento de Matemática', 'D002', '987654321', 'Centro de Ciências');

INSERT INTO CURSO (nome, tipo, id_departamento, coordenador, vice_coordenador) VALUES
('Ciência da Computação', 'Graduação', 1, 'Dr. João', 'Prof. Ana'),
('Engenharia de Software', 'Graduação', 1, 'Dr. Carlos', 'Prof. Lucia');

INSERT INTO ALUNO (nome, numero_matricula, cpf, endereco_rua, endereco_cidade, endereco_cep, telefone, data_nascimento, sexo, id_departamento, id_curso) VALUES
('Lucas Silva', '2025001', '12345678901', 'Rua A, 123', 'São Paulo', '01001000', '123456789', '2000-03-15', 'M', 1, 1),
('Mariana Oliveira', '2025002', '98765432100', 'Rua B, 456', 'Rio de Janeiro', '02002000', '987654321', '1999-07-20', 'F', 2, 2);

INSERT INTO DISCIPLINA (nome, descricao, codigo, numero_creditos, id_departamento) VALUES
('Programação I', 'Introdução à programação', 'COMP101', 4, 1),
('Matemática Discreta', 'Fundamentos de lógica e conjuntos', 'MATH101', 4, 2);

INSERT INTO MATRICULA (id_aluno, id_oferta) VALUES
(1, 1),
(2, 2);

SELECT * FROM DEPARTAMENTO;
SELECT * FROM CURSO;
SELECT * FROM ALUNO;
SELECT * FROM PROFESSOR;
SELECT * FROM DISCIPLINA;
SELECT * FROM OFERTA_DISCIPLINA;
SELECT * FROM MATRICULA;











