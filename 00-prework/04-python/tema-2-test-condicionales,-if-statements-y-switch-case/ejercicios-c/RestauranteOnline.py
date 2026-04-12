
'''
En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
Los ingredientes extra de la hamburguesa clásica son:
- Queso Idiazabal
- Bacon
- Huevo
Los ingredientes extra de la hamburguesa vegana son:
- Tofu
- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la
respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos.
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus
ingredientes. 
'''

# Pedimos al usuario que hamburguesa quiere
tipo_hamburguesa = input("¿Qué tipo de hamburguesa quieres? (clásica/vegana): ").strip().lower()

# Definimos los ingredientes extra para cada tipo de hamburguesa
if tipo_hamburguesa == "clásica":
    ingredientes_extra = ["Queso Idiazabal", "Bacon", "Huevo"]
elif tipo_hamburguesa == "vegana":
    ingredientes_extra = ["Tofu", "Cebolla caramelizada"]
else:
    print("Tipo de hamburguesa no válido.")
    exit()

# Mostramos los ingredientes extra disponibles
print("Ingredientes extra disponibles:")
for i, ingrediente in enumerate(ingredientes_extra, start=1):
    print(f"{i}. {ingrediente}")

# Pedimos al usuario que elija un ingrediente extra
eleccion = int(input("Elige un ingrediente extra (número): ")) - 1

# Verificamos que la elección sea válida
if 0 <= eleccion < len(ingredientes_extra):
    ingrediente_elegido = ingredientes_extra[eleccion]
    print(f"Has elegido la hamburguesa {tipo_hamburguesa} con el ingrediente extra {ingrediente_elegido}.")
else:
    print("Elección no válida.")
