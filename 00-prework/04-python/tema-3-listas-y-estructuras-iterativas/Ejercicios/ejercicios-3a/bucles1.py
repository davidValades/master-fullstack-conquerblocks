'''Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura. 


*
**
***
****
*****
****
***
**
*
'''

# --- Pedimos al usuario un número entero
numero = int(input("Introduce un número entero: "))
# --- Creamos un bucle for para mostrar la estructura de estrellas
for i in range(1, numero + 1):
    print("*" * i)
for i in range(numero - 1, 0, -1):
    print("*" * i)

    