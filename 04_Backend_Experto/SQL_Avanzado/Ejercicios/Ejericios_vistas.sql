/*
Dentro de la base de datos academia
1. Crea una vista llamada ‘cursos_precio_alto’ con los cursos cuyo precio sea
superior a 150
2. Crea una vista llamada ‘cursos_alumno’ que tengan las columnas nombre del
curso y nombre del alumno. Tiene que aparecer el alumno y sus cursos
3. Crea una vista llamada ‘asignaturas_curso’ en la que aparezcan los cursos con
las asignaturas que tienen. En este caso las columnas se llamarán
“Asignatura” y “curso”. Los nombres de las columnas deben ser creadas en la
declaración de la vista. También debe estar ordenado por el nombre del curso.
4. Intenta insertar un nuevo curso a través de la vista ‘cursos_precio_alto’
5. Intenta hacer lo mismo con ‘asignaturas_curso’
6. ¿Y si le ponemos todas las columnas de las tablas asignaturas y cursos?
7. Vamos ahora a probar el Check Option. Vamos a insertar una fila en la vista
“cursos_precio_alto” que sea de un curso que no cumpla la condición (precio
> 150) ¿funciona?
8. Introduce un check option ahora
9. Intenta insertar una fila que no cumpla las condiciones

*/

Select * from cursos;

-- Ejercicio 1
CREATE OR REPLACE VIEW cursos_precio_alto as
SELECT * FROM cursos WHERE
PRECIO > 150;

-- Ejercicio 2

CREATE OR REPLACE VIEW cursos_alumnos(nombre_alumno, nombre_curso) as
SELECT alumnos.nombre_alumno, cursos.nombre_curso from alumnos
inner join cursos
ON ALUMNOS.ID_ALUMNO = CURSOS.ID_CURSO;

-- Ejercicio 3

CREATE OR REPLACE VIEW asignaturas_curso(Asignatura, Curso) as
SELECT asignaturas.nombre_asignatura, cursos.nombre_curso 
FROM asignaturas join cursos
ORDER BY nombre_curso;

-- Ejercicio 4
INSERT INTO CURSOS_PRECIO_alto VALUES(99, "nuevo_curso", 200);

-- Ejercicio 5
INSERT INTO ASIGNATURAS_CURSO VALUES('CURSO99, ASIGNATURA_1')
/* EN ESTE CASO NO DEJA YA QUE NO APARECEN EN LA VISTA LAS COLUMNAS NECESARIAS */

-- Ejercicio 6
INSERT INTO asignaturas_curso (CURSO.ID_CURSO, CURSOS.NOMBRE_CURSO, CURSO.PRECIO
ASIGNATURAS.ID_ASIGNATURA, ASIGNATURAS.NOMBRE_ASIGNATURA, ASIGNATURA.ID_CURSO)
VALUES
(100, 'CURSO100', 200, 100, 'ASIGNATURA100', 100, 4, 10);
/* TAMPOCO DEJA PORQUE AUNQUE PONGAMOS LAS ROW QUE SE NECESITA, LAS VISTAS NO LOS CONTIENE */

-- Ejercicio 7
INSERT INTO CURSOS_PRECIO_ALTO VALUES (100, 'CRUSO100', 130);
SELECT * FROM CURSOS_PRECIO_ALTO;
SELECT * FROM CURSOS;

-- Ejercicio 8
CREATE OR REPLACE VIEW CURSOS_PRECIO_ALTO AS SELECT * FROM CURSOS WHERE PRECIO>150 WITH CHECK OPTION;

-- Ejercicio 9
INSERT INTO CURSOS_PRECIO_ALTO VALUES(101, 'CURSO101', 190);
SELECT * FROM CURSOS_PRECIO_ALTO;