CREATE DATABASE catrina;

USE catrina;

CREATE TABLE usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(32) NOT NULL,     
    sobrenome VARCHAR(32) NOT NULL,
    nome_usuario VARCHAR(15) UNIQUE NOT NULL,
    senha CHAR(15) NOT NULL,
    criacao TIMESTAMP NOT NULL CURRENT_TIMESTAMP,
    PRIMARY KEY (criacao)
)