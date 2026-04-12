'''
1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa.
2. Usa la función len() para imprimir la longitud de la lista frutas.
3. Accede al objeto numero 3 de la lista e imprímelo or consola.
4. Modifica el segundo objeto de la lista y cambiado a mora.
5. Añade el string mango al final de la lista.
6. Usa el método insert() y añade el string “uva“ año comienzo de la lista.
7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
llamada “ultima_fruta“.
9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
tengan más de 5 caracteres
12. Usa el método remove() para borrar el string “cereza“ de la lista.
13. Usa el método clear() para vaciar la lista.
Recomendación: En cada paso comprueba que el código hace aquello que quieres 
'''

# --- Crea una lista llamada frutas

frutas = ["manzana", "plátano", "cereza", "pera", "higo", "frambuesa", "fresa"]

# --- 2. Usa la función len() para imprimir la longitud de la lista frutas

print(len(frutas))

# --- 3. Accede al objeto numero 3 de la lista e imprímelo or consola
print(frutas[2])

# --- 4. Modifica el segundo objeto de la lista y cambiado a mora
frutas[1] = "mora"

# --- 5. Añade el string mango al final de la lista
frutas.append("mango")

# --- 6. Usa el método insert() y añade el string “uva“ año comienzo de la lista
frutas.insert(0, "uva")

# --- 7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
for fruta in frutas:
    print(fruta)

# --- 8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable llamada “ultima_fruta“.
ultima_fruta = frutas.pop()
print(ultima_fruta)

# --- 9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
for fruta in frutas:
    print(fruta)

# --- 10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
for fruta in frutas:
    print(fruta, len(fruta))

# --- 11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que tengan más de 5 caracteres
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)

# --- 12. Usa el método remove() para borrar el string “cereza“ de la lista.
frutas.remove("cereza")

# --- 13. Usa el método clear() para vaciar la lista.
frutas.clear()
print(frutas)
print(ultima_fruta)

