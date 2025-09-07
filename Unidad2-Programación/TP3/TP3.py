# 1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# 2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3)Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". 

num = int(input("Ingrese un numero: "))
while num % 2 != 0:
    print("Por favor, ingrese un numero par")
    num = int(input ("Ingrese un numero: "))
print("Ha ingresado un numero par")

# 4)Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Es Niño/a")
elif edad >= 12 and edad < 18:
    print("Es Adolescente")
elif edad >= 18 and edad < 30:
    print("Es Adulto joven")
else:
    print("Eres adulto")

# 5)Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
# imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, 
# ingrese una contraseña de entre 8 y 14 caracteres".

clave = input("Ingrese una contraseña que contenga entre 8 a 14 caracteres: ")
if 8<= len (clave) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor,ingrese una contraseña de entre 8 y 14 caracteres")

# 7)Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e 
# imprimir el string resultante por pantalla; en caso contrario, 
# dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla

frase = input("Ingrese una frase o palabra: ")
ultima_letra = frase[-1].lower()
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(frase + "!")
else:
    print(frase)

# 8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla.

nombre = input("Ingrese su nombre: ")
print("Seleccione una opción para transformar su nombre:")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro")
opcion = input("Ingrese 1, 2 o 3: ")
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Debe ingresar 1, 2 o 3.")

#  9)Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    magnitud_terremoto >= 7
    print("Extremo (puede causar graves daños a gran escala)")

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese su hemisferio (N para norte, S para sur): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 12 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 3 or dia <= 20)):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 6 or dia <= 20)):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 12 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 3 or dia <= 20)):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 6 or dia <= 20)):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

print("Se encuentra en Estación:", estacion)