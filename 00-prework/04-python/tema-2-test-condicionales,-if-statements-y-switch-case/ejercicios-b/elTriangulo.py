# Crea un script que dado tres longitudes indique si podria construirse un triangulo con esos numeros.

a=float(input("Ingrese la primera longitud: "))
b=float(input("Ingrese la segunda longitud: "))
c=float(input("Ingrese la tercera longitud: "))

if a < b + c and b < a + c and c < a + b:
    print("Se puede construir un triángulo con esas longitudes.")
else:
    print("No se puede construir un triángulo con esas longitudes.")