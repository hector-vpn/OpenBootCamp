/*
TIPOS DE DATOS

int                     ENTERO
integer                 ENTERO
varchar                 STRING
char                    STRING
float                   DECIMAL
date, time, timestamp   DATOS DE FECHA Y HORA

//STRINGS MAS GRANDES
TEXT            (65535 CARACTERES)
MEDIUMTEXT      (16 MILLONES CARACTERES)
LONGTEXT        (4 BILLONES DE CARACTERES)
*/

/*
creando una tabla en la BD.
*/

CREATE TABLE usuarios(
id          int(11) auto_increment not null,
nombre      varchar(100)not null,
apellidos   varchar(255)default('Saucedo'),
email       varchar(100)not null,
password    varchar(255),
CONSTRAINT pk_usuarios PRIMARY KEY(id)
);