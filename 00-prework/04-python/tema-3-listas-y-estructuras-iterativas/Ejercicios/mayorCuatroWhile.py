'''Pide al usuario 4 numeros y devuelve
los numeros introducidos en orden ascendente
Para ello puedes usar listas y bucles for
'''

# iniciamos una lista de numeros
numeros = []
# --- Creamos un bucle while para ir pidiendo los numeros al usuario y añadiendolos a la lista
i = 0
while i < 4:
    numero = (input("Introduce un número: "))
    numeros.append(numero)
    i += 1

# --- Ordenamos la lista de numeros de menor a mayor
numeros.sort()

print("Los números introducidos en orden ascendente son: ", numeros) 

