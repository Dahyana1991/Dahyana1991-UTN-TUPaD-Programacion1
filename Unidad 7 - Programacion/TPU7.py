## 1) Dado el diccionario precios_frutas
## precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
## Añadir las siguientes frutas con sus respectivos precios:
## ● Naranja = 1200
## ● Manzana = 1500
## ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de añadir:", precios_frutas)

## 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
## desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
## ● Banana = 1330
## ● Manzana = 1700
## ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario después de actualizar:", precios_frutas)

## 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
## desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios

lista_frutas = list(precios_frutas.keys())

print("Lista de frutas:", lista_frutas)

## 4) Escribí un programa que permita almacenar y consultar números telefónicos.
## • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
## • Luego, pedí un nombre y mostrale el número asociado, si existe.

def programa_telefonos():
    agenda = {}
    NUM_CONTACTOS = 5

    print(f" Carga de {NUM_CONTACTOS} contactos ")
    for i in range(NUM_CONTACTOS):

        nombre = input(f"Ingrese el nombre del contacto {i+1}: ").strip()
     
        numero = input(f"Ingrese el número telefonico de {nombre}: ").strip()

        agenda[nombre] = numero
    
    print("\n Carga de contactos finalizada ")
    print("Agenda actual:", agenda)


    print("\n Consulta de numero telefonico ")
    nombre_consulta = input("Ingrese el nombre del contacto q desea consultar: ").strip()


    if nombre_consulta in agenda:
     
        numero_asociado = agenda[nombre_consulta]
        print(f"El numero de telefono de {nombre_consulta} es: {numero_asociado}")
    else:
      
        print(f" error el contacto '{nombre_consulta}' no se encontro en la agenda.")


programa_telefonos()

## 5) Solicita al usuario una frase e imprime:
## • Las palabras únicas (usando un set).
## • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("ingresa una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)
print("las palabras unicas:")
print(palabras_unicas)

frecuencia_palabras = {}
for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print(" diccionario con la cantidad de veces que aparece cada palabra:")
print(frecuencia_palabras)

## 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
## Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    
    print("Ingresá sus 3 notas:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPROMEDIOS DE LOS ALUMNOS:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")

## 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
## y Parcial 2:
## • Mostrá los que aprobaron ambos parciales.
## • Mostrá los que aprobaron solo uno de los dos.
## • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobados_parcial1 = {1, 2, 3, 4, 5}
aprobados_parcial2 = {6, 7, 8, 9, 10}

print("Aprobados Parcial 1:", aprobados_parcial1)
print("Aprobados Parcial 2:", aprobados_parcial2)

ambos = aprobados_parcial1 & aprobados_parcial2
print("\nAprobaron AMBOS:", ambos)

solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Aprobaron SOLO UNO :", solo_uno)

al_menos_uno = aprobados_parcial1 | aprobados_parcial2
print("Aprobaron AL MENOS UNO :", al_menos_uno)

## 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
## Permití al usuario:
## • Consultar el stock de un producto ingresado.
## • Agregar unidades al stock si el producto ya existe.
## • Agregar un nuevo producto si no existe.

inventario = {}

while True:
    print("\n--- Gestión de Inventario ---")
    print("1. Consultar Stock")
    print("2. Agregar/Actualizar Stock")
    print("3. Ver Inventario")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ")
        stock = inventario.get(producto, "Producto no encontrado") 
        if stock != "Producto no encontrado":
            print(f"El stock actual de **{producto}** es: **{stock}**")
        else:
            print(stock)

    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        
        if producto in inventario:
           
            inventario[producto] += unidades
            print(f"Se agregaron {unidades} unidades. Nuevo stock de {producto}: {inventario[producto]}")
        else:
            
            inventario[producto] = unidades
            print(f"Producto **{producto}** agregado al inventario con stock inicial de {unidades}.")
    
    elif opcion == '3':
        print("\nInventario actual:", inventario)

    elif opcion == '4':
        print("Saliendo del programa de inventario.")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")

## 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
## Permití consultar qué actividad hay en cierto día y hora

agenda = {
    ("lunes", "11:00"): "Parcial",
    ("viernes", "15:00"): "Videollamada trabajo"
}

dia = input('Ingrese el dia: ')
hora = input('Ingrese la hora: ')
evento = agenda.get((dia, hora), 'No hay evento en ese dia y hora')
print(evento)

## 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
## diccionario donde:
## • Las capitales sean las claves.
## • Los países sean los valores.

paises_capitales = {
    "Estados Unidad": "Washington D.C",
    "Francia": "París",
    "Colombia": "Bogotá",
    "Italia": "Roma",
    "Austria": "Viena"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print(f"Diccionario Original: {paises_capitales}")
print(f"Nuevo Diccionario (Invertido): {capitales_paises}")