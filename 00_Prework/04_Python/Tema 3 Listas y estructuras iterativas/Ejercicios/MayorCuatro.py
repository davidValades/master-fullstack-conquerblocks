'''Pide al usuario 4 numeros y devuelve
los numeros introducidos en orden ascendente
Para ello puedes usar listas y bucles for
'''

#Iniciamos una lista de numeros

numeros = []
# --- Creamos un bucle for para ir pidiendo los numeros al usuario y añadiendolos a la lista
for i in range(4):
    numero = (input("Introduce un número: "))
    numeros.append(numero)

# --- añadimos a la lista
numeros.append(numero)
1
# --- Ordenamos la lista de numeros de menor a mayor
numeros.sort()

print("Los números introducidos en orden ascendente son: ", numeros)