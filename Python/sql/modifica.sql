#Renombra una tabla

ALTER TABLE usuarios RENAME TO usuarios_1;

#Cambiar el nombre de una colomna

ALTER TABLE usuarios_1 CHANGE apellidos apellido varchar(100) null;

#Modificar una columna sin cambiar el nombre

ALTER TABLE usuarios_1 MODIFY apellido char(50) not null;

#Añadir colomna a una tabla

ALTER TABLE usuarios_1 ADD website varchar(100) null;

#Añadir una restriccion a columnas
ALTER TABLE usuarios_1 ADD CONSTRAINT uq_email UNIQUE(email);

#Borrar una columna

ALTER TABLE usuarios_1 DROP website;