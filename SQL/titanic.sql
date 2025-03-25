create database Titanic;
use Titanic;
create table titanic_base (
PassengerId int primary key,
Survived int,
Pclass int,
Nome varchar(50),
Sex varchar(20),
Age int,
SibSp int,
Parch int,
Ticket int,
Fare int,
Cabin varchar(20),
Embarked varchar(10)

);
 