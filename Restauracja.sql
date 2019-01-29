create database Restauracja;
use Restauracja;

CREATE TABLE logowanie (
  id         int(11) NOT NULL AUTO_INCREMENT,
  login      varchar(30) NOT NULL,
  passwd     varchar(45) NOT NULL,
  PRIMARY KEY (id)
);
drop table pizza;
CREATE TABLE pizza (
	id			int(11) not null Auto_increment,
    nazwa 		varchar(20) not null,
    skladniki 	varchar(20) not null,
    Cena		Varchar(5) not null,
    PRIMARY KEY (id)
);
drop table Zupy
CREATE TABLE zupy (
	id			int(11) not null Auto_increment,
    nazwa 		varchar(20) not null,
    skladniki 	varchar(20) not null,
    Cena		Varchar(5) not null,
    PRIMARY KEY (id)
);
drop table Dania;
Create Table dania (
	id			int(11) not null Auto_increment,
    nazwa 		varchar(20) not null,
    skladniki 	varchar(30) not null,
    Cena		Varchar(5) not null,
    PRIMARY KEY (id)
)
drop table Kontakt
Create table kontakt (
	cel		varchar(20) not null,
    numer	varchar(20) not null
);
    
insert into logowanie values (1, "Pracownik1", "Pracownik1");
insert into logowanie values (2, "Pracownik2", "Pracownik2");
insert into logowanie values (3, "Pracownik3", "Pracownik3");


insert into pizza values(1, "margharita", "ser","25PLN");
insert into pizza values(2, "pepperoni", "ser,pepperoni","30PLN");
insert into pizza values(3, "diabolo", "ser, bekon, chilli","35PLN");


insert into Zupy values(1, "pomidorowa", "bulion, pomidory", "15PLN");
insert into Zupy values(2, "ogórkowa", "bulion, ogórki", "20PLN");
insert into Zupy values(3, "szczawiowa", "bulion, szczaw", "25PLN");

insert into Dania values(1, "Special dnia", "ziemniaki, kotlet schabowy", "15PLN");
insert into Dania values(2, "Danie polskie", "bigos, kotlet mielony", "20PLN");
insert into Dania values(3, "Danie studenckie", "chleb posmarowany nożem", "5PLN");

insert into Kontakt values("Rezerwacja stolika", "123456789");
insert into Kontakt values("Rezerwacja sali", "987654321");

select * from logowanie;