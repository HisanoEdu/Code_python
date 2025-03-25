
use matricula;

create table aluno (
    idAluno int auto_increment primary key,
    nome varchar(100) not null,  
    curso_id int,
    foreign key (curso_id) references curso (idCurso)
);

create table curso (
    idCurso int auto_increment primary key,
    nome varchar(30) not null,
    
    faculdade_id int,
    foreign key (faculdade_id) references faculdade (idFaculdade)
);

create table turma (
    idTurma int auto_increment primary key,
    periodo_letivo_id int,
    disciplina_id int,
    professor_id int,
    foreign key (periodo_letivo_id) references periodoLetivo (idPeriodoLetivo),
    foreign key (disciplina_id) references disciplina (idDisciplina),
    foreign key (professor_id) references professor (idProfessor) 
);

create table disciplina (
    idDisciplina int auto_increment primary key,
    nome varchar(50) not null 
);

create table periodoLetivo (
    idPeriodoLetivo int auto_increment primary key,
    ano int not null, 
    semestre int not null
);

create table faculdade (
    idFaculdade int auto_increment primary key,
    nome varchar (30) not null, 
    instituto_id int,
    foreign key (instituto_id) references instituto (idInstituto)
);

create table instituto (
    idInstituto int auto_increment primary key,
    nome varchar(30) not null 
);

create table professor (  
    idProfessor int auto_increment primary key,
    nome varchar(100) not null
);


create table aluno_turma (
    aluno_id int,
    turma_id int,
    foreign key (aluno_id) references aluno (idAluno),
    foreign key (turma_id) references turma (idTurma),
    primary key (aluno_id, turma_id) 
);


describe aluno;
describe curso;
describe turma;
describe disciplina;
describe periodoLetivo;
describe faculdade;
describe instituto;
describe professor;
describe aluno_turma;
