## 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
## función para calcular y mostrar en pantalla el factorial de todos los números enteros
## entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


## 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
## indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Ingrese la cantidad de términos: "))
for i in range(num):
    print(fibonacci(i), end=" ")
print()

## 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
## exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

## 4) Crear una función recursiva en Python que reciba un número entero positivo en base
## decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario_recursivo(n):
    
    if n == 0:
        return ""
    
    cociente = n // 2
    resto = n % 2
    
    return decimal_a_binario_recursivo(cociente) + str(resto)

def probar_decimal_a_binario():
    
    num = int(input("Ingrese un número entero positivo en base decimal: "))
    
    if num == 0:
        print("El número 0 en binario es: 0")
    else:
        resultado_binario = decimal_a_binario_recursivo(num)
        print(f"El número {num} en binario es: {resultado_binario}")

## 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
## cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
## Requisitos:
##La solución debe ser recursiva.
## No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")

## 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
## número entero positivo y devuelva la suma de todos sus dígitos.
## Restricciones:
## No se puede convertir el número a string.
## Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


num = int(input("Ingrese un número: "))
print(f"La suma de sus dígitos es {suma_digitos(num)}")

## 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
## bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
## último nivel con un solo bloque.
## Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
## nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


niveles = int(input("Ingrese el número de bloques en el nivel inferior: "))
print(f"Total de bloques: {contar_bloques(niveles)}")

## 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
## número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
## aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


num = int(input("Ingrese un número: "))
n = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {n} aparece {contar_digito(num, n)} veces.")  