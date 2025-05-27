#Diccionarios
#Es una estructura de datos que almacena pares clave:valor. Es ideal para representar datos estructurados como usuarios,inventarios,configuraciones,etc.

#ejemplo
persona = {"nombre": "Ana", "Edad": 30, "ciudad" : "Santiago"}

##Cuando usar?

#Cuando necesitas asociar un valor a una clave unica (como nombre y edad)
#Cuando buscas acceder rapidamente a datos mediante una clave.
#Cuando necesitas almacenar información compleja de forma organizada.
#Alternativa a multiples variables individuales.

##Conceptos

#Clave (key) / identificador unico / "nombre"
#Valor (value) / Dato asociado a la clave / "Ana"
#Par clave:valor / Unidad básica / "edad" : 30

##Crear diccionarios

#Vacio
mi_dic = {}

#Con datos
alumno = {"Nombre":"Perdro","Nota" : 6.5}

#usando dict()
otro_dict = dict(nombre="Laura",edad=28)

#Acceder y modificar elementos.
print(alumno["Nombre"]) #Accede
alumno["Nota"] = 7.0 #Modifica
alumno["Curso"] = "Python" #Agrega nuevo par


##Metodos utiles en diccionarios.

#.get(clave) / obtiene valor (retorna none si no existe)
alumno.get("nombre")

#.keys() #Retorna todas las claves.
alumno.keys()

#.values() / Retorna todos los valores
alumno.values()

#.items() / Retorna pares (clave:valor)
alumno.items()

#.update() /Actualiza/añade pares de clave:valor
alumno.update({"ciudad":"Viña del Mar"})

#.pop(clave) /Elimina clave y retorna su valor
alumno.pop("nota")

#.clear() / Vacía el diccionario
alumno.clear()

## Recorrer diccionarios

#Claves
for clave in alumno:
    print(clave)

# Claves y valores:
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")


## Diccionarios anidados.

usuarios = {
    "Usuario1" : {"Edad":25,"Estatura":1.75},
    "Usuario2" : {"Edad":30,"Estatura":1.50}
}

print(usuarios["Usuario1"]["Edad"])

##Ejemplo de aplicación practica.

productos = {}
productos["001"] = {"nombre":"Leche","Precio": 1200}
productos["002"] = {"nombre":"Pan","Precio": 800}

for codigo,datos in productos.items():
    print(f"Codigo: {codigo}, Producto: {datos["nombre"]}, Precio: {datos["Precio"]}")