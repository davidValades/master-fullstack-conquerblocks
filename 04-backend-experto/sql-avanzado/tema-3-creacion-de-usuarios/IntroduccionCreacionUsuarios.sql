/* 

INTRODUCCION A LA SEGURIDAD

CREAR USUARIOS --> COMO CREAR Y MODIFICAR CONTRASEÑAS
	usuario@host
    'usuario'@'host' <-- buenas practicas
    Ejemplo:
    'usuario1'@'190.168.10.1'
	'usuario1'@'190.168.10.12' 
    
    'usuario1'@'%' <-- permite conectar desde cualquier maquina
    'usuario1'@'190.168.1.%' <-- permite conectar con un rango de IP
    
PRIVILEGIOS Y LOS PERMISOS

ROLES

*/

-- CREATION DE USUARIOS --

CREATE USER 'USER1'@'%' IDENTIFIED BY 'prueba';

CREATE USER 'USER2'@'190.168.10.12' IDENTIFIED BY 'prueba';

SELECT * FROM mysql.user; -- para ver los usuarios que hay en la base de datos --

SET PASSWORD FOR 'USER1'@'%' = 'password'; -- para cambiar contraseña de un usuario --
ALTER USER 'USER1'@'%' IDENTIFIED BY 'prueba2'; -- otra manera de cambiar contraseña de usuario --