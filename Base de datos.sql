CREATE DATABASE proyecto_normalización;
CREATE DATABASE IF NOT EXISTS proyecto_normalizacion;
USE proyecto_normalización;

CREATE TABLE sexo (
	id_sexo INT auto_increment primary KEY,
    nombre VARCHAR (40) NOT NULL UNIQUE
	);
    
CREATE TABLE nivel_educativo (
	id_nivel_educativo INT auto_increment primary KEY,
    nombre VARCHAR (80) NOT NULL UNIQUE
);

CREATE TABLE persona (
	id_persona INT auto_increment PRIMARY KEY,
    edad INT ,
    id_nivel_educativo INT,
    años_esc INT,
    ingreso_mensual DECIMAL (12,2),
    id_sexo INT,
    FOREIGN KEY (id_sexo) REFERENCES sexo (id_sexo),
    FOREIGN KEY (id_nivel_educativo) REFERENCES nivel_educativo (id_nivel_educativo)
    );
