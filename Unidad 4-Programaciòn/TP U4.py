# 1)Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range (101):
    print(numero)

# 2)Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = input ("Ingrese un numero entero: ")
cantidad_digitos = len (numero)

print(f"El numero {numero} tiene {cantidad_digitos} digitos")

# 3)Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un primer numero entero: " ))
num2 = int(input("Ingrese un segundo numero entero: " ))

suma = 0
for numero in range (min(num1,num2) + 1, max(num1,num2)):
    suma += numero
print(f"La suma de los numeros entre {num1} y {num2}, excluyendo ambos, es: {suma}")

# 4)Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total = 0
numero = int(input("Ingrese un número entero (0 para finalizar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingrese un número entero (0 para finalizar): "))

print(f"El total acumulado es: {total}")



# 5)Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

entrada = input("Escribe una palabra o un número: ")
numero_secreto = len(entrada) % 10 
intentos = 0
intento = -1

while intento != numero_secreto:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intentos.")
    else:
        print("Incorrecto, intenta de nuevo.")
                                  


# 6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -2):
    print(numero)   


# 7)Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero positivo: "))
suma = 0    
for numero in range(num + 1):
    suma += numero  
print(f"La suma de los numeros entre 0 y {num} es: {suma}")

# 8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. 
 
pares = 0
impares = 0     
positivos = 0
negativos = 0

cantidad = 100
contador = 0

while contador < cantidad:
    numero = int(input("Ingrese un numero entero: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    contador += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


# 9)Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.

suma = 0
cantidad = 100
contador = 0

while contador < cantidad:
    numero = int(input("Ingrese un número entero: "))
    suma += numero
    contador += 1

media = suma / cantidad
print(f"La media de los {cantidad} números ingresados es: {media}")

# 10)Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número entero: "))
n = abs(numero) 
invertido = 0

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10
if numero < 0:
    invertido = -invertido

print(f"El número invertido es: {invertido}")