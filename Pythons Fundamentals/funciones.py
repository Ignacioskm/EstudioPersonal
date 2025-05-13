# Funciones

#pass = sirve para que la funcion no haga nada.

#Ejemplo
# def nombre_funcion():
#     pass

# nombre_funcion

#Funcion para saludar
# def saludar():
#     print("Hola")

# saludar()

# #Dentro de los parentesis podemos darle argumentos.
# def saludar(nombre):
#     print(f"Hola {nombre}")

# saludar("BitBoss") #En este caso cuando llamamos a la funcion le damos el argumento bitboss

## Nonetype = es un valor similar a los bolooanos representa que hay ausencia osea que no hay nada.


#Funcion para calcular el promedio.
# def promedio(nota1,nota2,nota3):
#     suma = nota1+nota2+nota3
#     promedio = suma/3
#     return promedio

# llamada = promedio(2,4,5)
# print(llamada)

##Se pudo haber optimizado todo en una sola linea de la siguiente manera
# def promedio_optimizado(nota1,nota2,nota3):
#     return (nota1+nota2+nota3)/3 #Esto se puede ya que return puede devolver tanto variables como expresiones

# llamada_optimizada = promedio_optimizado(2,4,5)
# print(llamada_optimizada)

#Diferencia entre print y return
#Print no es mas que una funcion para visualizar, te sirve como dev para depurar o para mostar al usuario
#Return es la sentencia que te permite utilizar valores calculados en las funciones.
#Si utilizas print en vez de return la llamada devolvera none por defecto.
#Con return devolvemos el resultado.

#El orden importa dentro de las funciones
# def resta(num1,num2):
#     return num1 - num2

# print(resta(5,3))
# print(resta(3,5))

#Pero hay una manera de especificar el orden con los Keyword Arguments
#Los Keyword Arguments son las palabras clave que le has dado a tus argumentos
#Ejemplo

# print(resta(num2 = 5, num1 = 3)) #Aqui nosotros estamos especificando que valor tomara el argumento.

#Scope , significa alcance se refiere al alcance de las variables
#Si tu en una funcion declaras una variable, esta variable solo existe dentro de la funcion (variable local)
#para poder acceder a una variable desde afuera a dentro de la funciona se ocupa la sentencia global


#Ejercicios: 

#Promedio de 3 Notas.
#Crea una función que reciba tres notas y devuelva su promedio.
def promedio_notas(nota1,nota2,nota3):
    if 1 <= nota1 <= 7  and 1 <= nota2 <= 7 and 1 <= nota3 <=7:
        return (nota1 + nota2 + nota3)/3
    else:
        print("Ingrese una nota dentro de 1 a 7")

nota1 = float(input("Ingrese la nota1: "))
nota2 = float(input("Ingrese la nota2: "))
nota3 = float(input("Ingrese la nota3: "))

print(f"Tu promedio de notas es: ",promedio_notas(nota1,nota2,nota3))

#Doble de un numero.
#Crea una función que reciba un número y retorne su doble.
def duplicar(num):
    return 2 * num

numero_a_duplicar = int(input("Ingrese el numero que deseas duplicar: "))
print(duplicar(numero_a_duplicar))

#Par o Impar
#Crea una función que reciba un número y devuelva True si es par, False si es impar.
def par_o_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese un numero para evaluar si es par o impar: "))
print(par_o_impar(numero))


#Conversor de temperatura.
#Crea una función que reciba una temperatura en grados Celsius y la convierta a Fahrenheit.
def conversor(temperatura):
    return (temperatura * 9/5) + 32

temperatura = int(input("Ingresa la temperatura que deseas transformar de Celcius a Fahrenheit: "))
print(conversor(temperatura))


#Area de un triangulo
#Crea una función que reciba la base y la altura de un triángulo y devuelva su área.
def calcular_area(base,altura):
    return (base * altura) / 2

base = int(input("Ingresa la base del triangulo: "))
altura = int(input("Ingresa la altura del triangulo: "))

print(calcular_area(base,altura))

#Nombre Completo
#Crea una función que reciba un nombre y un apellido, y devuelva el nombre completo en una sola cadena.
def nombre_completo(nombre,apellido):
    return nombre + " " + apellido

nombre = input("Ingrese su primer nombre: ")
apellido = input("Ingrese su apellido: ")

print("Bienvenido ",nombre_completo(nombre,apellido))

#Total con iva(19%)
#Crea una función que reciba el precio de un producto y devuelva el total con IVA incluido.
def calcular_iva(precio):
    return precio * 1.19

precio = int(input("Ingrese el precio de su producto: "))

print(calcular_iva(precio))

#Clasificador de Numeros
#Crea una función que reciba un número y retorne si es "Positivo", "Negativo" o "Cero".
def clasificador_numeros(num_a_clasificar):
    if num_a_clasificar > 0:
        print("Es positivo")
    elif num_a_clasificar < 0:
        print("Es Negativo")
    else:
        print("Es 0")

num_a_clasificar = int(input("Ingrese el numero a clasificar: "))

clasificador_numeros(num_a_clasificar)

#Saludo Personalizado
#Crea una función que reciba un nombre y retorne un saludo como "Hola, [nombre]!".
def saludo(nickname):
    return f"Hola {nickname}!"

nickname = input("Ingresa tu nickname: ")

saludo(nickname)

#Promedio de una lista de notas
#Crea una función que reciba una lista de notas y devuelva el promedio.

#Lista
notas = []

#Funcion para calcular promedio
def calcular_promedio_notas(notas):
    suma = sum(notas)
    promedio_lista_notas = suma / len(notas)
    return promedio_lista_notas

#While menu para agregar notas.
while True:
    print("Bienvenido al sistema de notas que deseas hacer?")
    print(f"[1] Agregar Nota\n[2] Ver notas\n[3] Calcular promedio\n[4] Salir del menu")
    opcion = int(input("Ingrese el numero correspondiente a la opción: "))
    match opcion:
        case 1:
            nota_a_agregar = float(input("Ingresa la nota que deseas agregar: "))
            notas.append(nota_a_agregar)
        case 2:
            for nota in notas:
                print(nota)
        case 3:
            if notas:
                print(f"El promedio de las notas es: ",calcular_promedio_notas(notas))
            else:
                print("No hay notas para calcular el promedio.")
        case 4:
            break
        case _:
            print("Ingrese una opcion valida!! (de 1 a 4.)")

print("Saliendo del programa")


