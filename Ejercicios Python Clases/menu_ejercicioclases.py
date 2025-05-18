#Variables
usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

#Funciones
def llamada(celular):
    if len(str(celular)) == 9 and str(celular)[0] == "9":
        return f"Relizando una llamada al numero +56{celular}"
    else:
        return f"Por favor, ingrese un número de 9 digitos y que comience en 9"

def correo(correo_electronico):    
    if "@" in correo_electronico:
        print(f"Correo: {correo_electronico} ingresado correctamente.")
        mensaje = input("Ingrese el mensaje que desea enviar:\n")
        print(f"Mensaje: {mensaje} \nEnviado satisfactoriamente.")
    else:
        print("Correo inválido. Debe contener '@'.")


def menu_usuario():
    while True:
        try:
            print(f"[1] Realizar Llamada \n[2] Enviar correo electrónico \n[3] Cerrar sesión")
            opcion_login = int(input("Selecciona una opción: "))
            match opcion_login:
                case 1: # Realizar llamada
                    celular = int(input("Ingrese un numero de celular (que empiece en 9 y que tenga 9 digitos): "))
                    print(llamada(celular))                           
                case 2: # Enviar Correo electronico
                    correo_electronico = input("Ingrese un correo electronico: ")
                    correo(correo_electronico)
                case 3: #Cerrar sesion
                    print("Cerrando sesion..\nVolviendo al menu principal..")
                    break
                case _:
                    print("Opcion invalida, intentelo denuevo..")
        except ValueError:
            print("Error, porfavor ingrese un numero.")


#Menu Principal.
while True:
    try:    
        print(f"-------Bienvenido al menu-------")
        print(f"[1] Iniciar sesión \n[2] Registar usuario\n[3] Salir")
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1: #Iniciar Sesion
                if usuario1 == None and usuario2 == None and usuario3 == None:
                    print("Es necesario registar un usuario.\nVolviendo al menu..")
                else:
                    usuario_ingresado = input("Ingrese usuario: ")
                    contraseña_ingresada = input("Ingrese contraseña: ")
                    if (usuario_ingresado == usuario1) and (contraseña_ingresada == contraseña1):
                        print(f"Iniciaste sesión satisfactoriamente.\nBienvenido {usuario1}!")
                        menu_usuario()
                    elif (usuario_ingresado == usuario2) and (contraseña_ingresada == contraseña2):
                        print(f"Iniciaste sesión satisfactoriamente.\nBienvenido {usuario2}!")
                        menu_usuario()
                    elif (usuario_ingresado == usuario3) and (contraseña_ingresada == contraseña3):
                        print(f"Iniciaste sesión satisfactoriamente.\nBienvenido {usuario3}!")
                        menu_usuario()
                    else:
                        print(f"Datos incorrectos \nVolviendo al menu...")

            case 2: #Registrar usuario
                if usuario1 == None:
                    usuario1 = input("Ingrese nombre de usuario: ")
                    contraseña1 = input("Ingrese contraseña nueva: ")
                elif usuario2 == None:
                    usuario2 = input("Ingrese nombre de usuario: ")
                    contraseña2 = input("Ingrese contraseña nueva: ")
                elif usuario3 == None:
                    usuario3 = input("Ingrese nombre de usuario: ")
                    contraseña3 = input("Ingrese contraseña nueva: ")
                else:
                    print("Hay demasiados usuarios registrados, porfavor vuelva mas tarde...")
            case 3: # Salir
                print("Cerrando el menu..")
                break
            case _:
                print("Ingrese una opción valida.")
    except ValueError:
        print("Error, porfavor ingrese un numero.")

    

