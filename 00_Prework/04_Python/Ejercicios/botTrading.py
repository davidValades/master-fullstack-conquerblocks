# Crea un script de manera que dado un precio introducido por el usuario, si el precio del producto esta por debajo de 100dolares, el bot imprima por pantalla
# la orden de compra. Si esta entre 100 y 150 euros(ambos incluidos) el bot debera imprimir la orden de hold.
# si el precio esta por encima de 150 deberá imprimir la orden de venta.

a= precio=float(input("Ingrese el precio del producto: "))
if a < 100:
    print("Orden de compra")
elif a >= 100 and a <= 150:
    print("Orden de hold")
else:
    print("Orden de venta")

