from usuarios import Usuarios

def main():
    base_de_datos = Usuarios("data.txt")
    
    while True:
        print("Opciones:")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Mostrar usuarios registrados")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            base_de_datos.registrar_usuario()
        elif opcion == "2":
            base_de_datos.iniciar_sesion()
        elif opcion == "3":
            base_de_datos.mostrar_usuarios()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()