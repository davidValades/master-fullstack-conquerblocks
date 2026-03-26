# Crea un script que pida al usuario 3 numeros diferentes y le indique si alguno de ellos es la suma de los otros dos.

a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
c=float(input("Ingrese el tercer número: "))

if a == b + c:
    print("El número ", a, " es la suma de ", b, " y ", c)
elif b == a + c:
    print("El número ", b, " es la suma de ", a, " y ", c)
elif c == a + b:
    print("El número ", c, " es la suma de ", a, " y ", b)
else:    print("Ningún número es la suma de los otros dos.")