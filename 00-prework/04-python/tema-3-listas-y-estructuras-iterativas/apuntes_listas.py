# -- Listas --

coches = ["BMW", "Mercedes", "Audi", "Ferrari"] # Las listas son mutables, lo que significa que podemos modificar su contenido después de haberlas creado.
numeros = [1, 2, 3, 4, 5] # Las listas pueden contener cualquier tipo de dato, incluso mezclados
cosas = ["Hola", 42, True, 3.14] # Las listas pueden contener otras listas, lo que se conoce como listas anidadas

print(coches) # Imprime la lista completa
print(coches[0]) # Imprime el primer elemento de la lista (BMW)
print(coches[1]) # Imprime el segundo elemento de la lista (Mercedes)
print(numeros) # Imprime la lista completa
print(cosas) # Imprime la lista completa


# append() -> Agrega un elemento al final de la lista.
print("Antes de agregar un nuevo coche: ", coches)
coches.append("Porsche") # Agrega "Porsche" al final de la lista de coches
print("Después de agregar un nuevo coche: ", coches)

# insert() -> Agrega un elemento en una posición específica de la lista.
print("Antes de insertar un nuevo coche: ", coches)
coches.insert(2, "Lamborghini") # Inserta "Lamborghini" en la posición 2 de la lista de coches
print("Después de insertar un nuevo coche: ", coches)

# pop() -> Elimina un elemento de la lista y lo devuelve. Si no se especifica un índice, elimina el último elemento.
print("Antes de eliminar un coche: ", coches)
coches.pop() # Elimina el último elemento de la lista de coches
print("Después de eliminar un coche: ", coches)
coches.pop(1) # Elimina el elemento en la posición 1 de la lista de coches (Mercedes)
print("Después de eliminar el coche en la posición 1: ", coches)

coches = ["BMW", "Mercedes", "Audi", "Ferrari"] # Reiniciamos la lista de coches
print(coches) # Imprime la lista completa
coche_eliminado = coches.pop(1) # Elimina el elemento en la posición 1 de la lista de coches (Mercedes) y lo guarda en la variable coche_eliminado
print("Después de eliminar el coche en la posición 1: ", coches) # Imprime la lista de coches después de eliminar Mercedes
print("El coche eliminado fue: ", coche_eliminado) # Imprime el coche que fue eliminado (Mercedes)  

# remove() -> Elimina la primera aparición de un elemento específico en la lista. Si el elemento no se encuentra, se genera un error.
print("Antes de eliminar un coche: ", coches)
coches.remove("Audi") # Elimina la primera aparición de "Audi" en la lista de coches
print("Después de eliminar el coche 'Audi': ", coches)

# del es una palabra reservada en Python que se utiliza para eliminar objetos. En el contexto de las 
# listas, se puede usar para eliminar un elemento en una posición específica o para eliminar toda la lista.
print("Antes de eliminar un coche: ", coches)
del coches[0] # Elimina el elemento en la posición 0 de la lista de coches (BMW)
print("Después de eliminar el coche en la posición 0: ", coches)
del coches # Elimina toda la lista de coches
# print(coches) # Esto generará un error porque la lista de coches ha sido eliminada


# ORDENAR LISTAS
# sort() -> Ordena los elementos de la lista en orden ascendente (de menor a mayor). Si la lista contiene cadenas de texto, se ordenarán alfabéticamente.
numeros = [5, 2, 9, 1, 3]
print("Antes de ordenar la lista de números: ", numeros)
numeros.sort() # Ordena la lista de números de menor a mayor
print("Después de ordenar la lista de números: ", numeros)

# si tengo una lista de cadena de texto con numeros, el ordenamiento se hará alfabéticamente, no numéricamente
numeros_str = ["5", "2", "9", "1", "3"]
print("Antes de ordenar la lista de números como cadenas de texto: ", numeros_str)
numeros_str.sort() # Ordena la lista de números como cadenas de texto alfabéticamente
print("Después de ordenar la lista de números como cadenas de texto: ", numeros_str)

# sorted() -> Devuelve una nueva lista ordenada sin modificar la lista original.
coches = ['bmw', 'mercedes', 'audi', 'ferrari']
print("Lista original de coches: ", coches)
print(sorted(coches)) # Devuelve una nueva lista de coches ordenada alfabéticamente

# reverse() -> Invierte el orden de los elementos en la lista.
coches = ['bmw', 'mercedes', 'audi', 'ferrari']
print("Antes de invertir el orden de la lista de coches: ", coches)
coches.reverse() # Invierte el orden de la lista de coches
print("Después de invertir el orden de la lista de coches: ", coches)

# len() -> Devuelve el número de elementos en la lista.
coches = ['bmw', 'mercedes', 'audi', 'ferrari']
print("Número de coches en la lista: ", len(coches)) # Devuelve el número

'''
ejercicios:
comprobar si un elemento está en una lista
'''

coches = ['bmw', 'mercedes', 'audi', 'ferrari']
coche_elegido = 'mercedes'
if coche_elegido in coches:
    print("El coche elegido está en la lista de coches")
else:    print("El coche elegido no está en la lista de coches")
