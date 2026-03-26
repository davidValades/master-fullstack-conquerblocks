# Crea un scipt que pida al usuario 4 números y muestre el mayor de ellos.

# Solución:

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
d = float(input("Ingrese el cuarto número: "))

if a >= b and a >= c and a >= d:
    print("El número mayor es: ", a)
elif b >= a and b >= c and b >= d:
    print("El número mayor es: ", b)
elif c >= a and c >= b and c >= d:
    print("El número mayor es: ", c)
else:
    print("El número mayor es: ", d)

