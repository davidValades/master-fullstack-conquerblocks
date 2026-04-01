/*
1. Crear un índice llamado i_nombre en la tabla cursos y columna “nombre”
2. Mostrar los índices de la tabla “cursos”
3. ¿Por qué aparecen dos?
4. Comprobar CON EXPLAIN que índice se usa la consultar por “nombre”
5. Borrar el índice
6. Volver a crearlo pero de tipo único y comprobar que se ha creado. La columna “Non unique” debe ser de tipo 0 (único).
7. Crear la siguiente tabla. Debemos crear los índices en el momento de creación
de la tabla. Después, comprobar la creación de estos índices
*/

USE ACADEMIA;

-- EJERCICIO 1--
CREATE INDEX i_nombre ON CURSOS(nombre_curso);

-- EJERCICIO 2--
SHOW INDEXES FROM CURSOS;

-- EJERCICIO 3 --
/* HAY 2 INDEXES PORQUE LA PRIMARY KEY GENERA YA UN INDICE DE FORMA AUTOMATICA */

-- EJERCIO 4 --
EXPLAIN SELECT * FROM CURSOS WHERE NOMBRE_CURSO = "CURSO100";

-- EJERCICIO 5 --
DROP INDEX I_NOMBRE ON CURSOS;

-- EJERCICIO 6 --
CREATE UNIQUE INDEX I_NOMBRE ON CURSOS(NOMBRE_CURSO);

-- EJERCICIO 7 --
CREATE TABLE TABLA_INDICES (
CODIGO INT PRIMARY KEY,
NOMBRE VARCHAR(50) UNIQUE,
APELLIDO VARCHAR(100),
INDEX NOMBRE_COMPLETO(NOMBRE, APELLIDO)
);

SHOW INDEXES FROM TABLA_INDICES;
