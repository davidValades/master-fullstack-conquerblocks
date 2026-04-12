/* 
INDICES
- Funcionalidad que sirve para poder buscar filas de una manera mucho mas rápida
- Nos permiten organizar los datos de forma que podamos buscarlos por la clave del indice
- Similar a un diccionario. Guardamos la clave y la posicion de la fila que posee es clavbe o valor
- Hay que actualizarlo cada vez que modificamos la tabla
- Tipo de indice:
	* Primary
    * Unique
    * Index normal
    * Fulltext
- El tipo de almacenamiento depende del tipo de indice
	* B-Tree es el mas habitual. Se suele usar para indices Primary, Unique, Fulltext...
    * R-Tree se utiliza para datos espaciales
    * HASH para índice de tablas en memoria
    
    */
    
CREATE SCHEMA INDICES;
USE INDICES;

CREATE TABLE DATOS_ALUMNO (
CODIGO INT,
NOMBRE VARCHAR(50),
APELLIDOS VARCHAR(100),
FECHA DATE);

-- CREAR UN INDEX
CREATE INDEX i_apellidos ON DATOS_ALUMNO(APELLIDOS);

-- PARA VER LOS INDICES
SHOW INDEXES FROM DATOS_ALUMNO;

-- SE PUEDEN CREAR VARIOS INDEX
CREATE INDEX i_nombre_completo ON DATOS_ALUMNO(APELLIDOS, NOMBRE);

-- COMANDO EXPLAIN
EXPLAIN SELECT * FROM DATOS_ALUMNO;

EXPLAIN SELECT * FROM DATOS_ALUMNO WHERE APELLIDOS ="GOMEZ";

EXPLAIN SELECT * FROM DATOS_ALUMNO WHERE NOMBRE ="NOMBRE" AND APELLIDOS ="GOMEZ";


CREATE TABLE DATOS_ALUMNOS2 (
CODIGO INT,
NOMBRE VARCHAR (50),
DNI VARCHAR(50),
CONSTRAINT PRIMARY KEY (CODIGO),
CONSTRAINT UNICO1 UNIQUE(DNI),
INDEX I_NOMBRE (NOMBRE)
);

SHOW INDEXES FROM DATOS_ALUMNOS2;

/*
CREACION DE INDICES UNICOS
*/

CREATE TABLE DATOS3(
CODIGO INT,
NOMBRE VARCHAR(50),
DNI VARCHAR(50)
);

CREATE UNIQUE INDEX I_DNI ON DATOS3(DNI);
SHOW INDEXES FROM DATOS3;

SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_NAME = "DATOS3";

-- CREATE primary INDEX I_CODIGO ON DATOS3(codigo); --> no se puede crear

CREATE TABLE DATOS4(
CODIGO INT,
NOMBRE VARCHAR(50),
DNI VARCHAR(20)
);

CREATE INDEX i_nombre ON DATOS4(NOMBRE(15));

EXPLAIN SELECT * FROM DATOS4 WHERE NOMBRE ="NOMBRE";

SHOW INDEXES FROM DATOS_ALUMNOS2;

-- PARA BORRAR INDICES: --

DROP INDEX UNICO1 ON DATOS_ALUMNOS2;
