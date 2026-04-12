# sintaxis while

while condicion:
    ejecucion_codigo

while (expr_logica) and (expr_logica2):
    ejecucion_codigo

# sintaxis for

for i in range(10):



# ejemplo temporizador

    import time

temporizador = int(input("Ingrese el tiempo en segundos: "))

print("Temporizador iniciado...")

while (temporizador > 0):
    print('Quedan', temporizador, 'segundos')
    time.sleep(1) # Pausa la ejecución del programa durante 1 segundo
    temporizador -= 1 # Resta 1 al valor del temporizador

print("¡Tiempo terminado!")

# ejemplo temporizador con for

temporizador = int(input("Ingrese el tiempo en segundos: "))

print("Temporizador iniciado...")

for i in range(temporizador, 0, -1): # El tercer argumento -1 indica que el contador se decrementará en 1 en cada iteración
    print('Quedan', temporizador, 'segundos')
    time.sleep(1)
    temporizador -= 1

print("¡Tiempo terminado!")

# Estructuras iterativas (como terminar un bucle)



while condition:
    set_instructions
    if condition_x:
        break # Termina el bucle while si se cumple la condición_x

set_instructions
