#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre=input("Ingresa tu Nombre: ")
print(f"Hola {nombre}!")

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre=input("Ingrese su Nombre: ")
apellido=input("Ingrese su Apellido: ")
edad=input("Ingrese su Edad: ")
lugar_residencia=input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido} , tengo {edad} años y vivo en {lugar_residencia}")

#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio=float(input("Ingrese el valor del radio de un circulo: "))
pi = 3.141592653589793
area = pi * radio **2
perimetro= 2 * pi * radio
print(f"El área del circulo es: {area} , y el perímetro es: {perimetro}")

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos= int(input("Ingrese la cantidad de segundos: "))
hora= segundos / 3600 
print(f"El equivalente en horas es" , {hora})

#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número
numero = int(input("Ingrese un número: "))
print(f"La tabla de multiplicar de ese número es:")
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1=int(input("Ingrese el primer numero Entero no nulo: "))
num2=int(input("Ingrese el segundo numero Entero no nulo: "))
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta= num1 - num2
print(f"El resultado de sumar {num1} con {num2} es: {suma}")
print(f"El resultado de dividir {num1} con {num2} es: {division}")
print(f"El resultado de multiplicar {num1} con {num2} es: {multiplicacion}")
print(f"El resultado de restar {num1} con {num2} es: {resta}")

#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
altura=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso: "))
imc=peso / (altura)**2
print(f"Su Indice de Masa Corporal es {imc}")

#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
temperatura=float(input("Ingrese su temperatura corporal en grados Celsius: "))
temp_fahrenheit= 9/5 * temperatura + 32
print(f"Su temperatura equivalente en grados Fahrenheit es {temp_fahrenheit}")

#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números
numero_1=float(input("Ingrese un primer numero: "))
numero_2=float(input("Ingrese un segundo numero: "))
numero_3=float(input("Ingrese un tercer numero: "))
promedio= (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio de los tres numeros ingresados es: {promedio}")
