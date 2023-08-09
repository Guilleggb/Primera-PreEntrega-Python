class Usuarios:
    def __init__(self, archivo):
        self.archivo = archivo
        self.base_de_datos = self.cargar_base_de_datos()

    def cargar_base_de_datos(self):
        try:
            with open(self.archivo, "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def guardar_base_de_datos(self):
        with open(self.archivo, "w") as f:
            for usuario in self.base_de_datos:
                f.write(usuario + "\n")

    def registrar_usuario(self):
        nombre = input("Ingrese un nombre de usuario: ")
        contrasenia = input("Ingrese su contraseña: ")

        usuario = f"Nombre : {nombre} | Contraseña : {contrasenia}"
        self.base_de_datos.append(usuario)
        print(f"\n***** El usuario {nombre} ha sido registrado exitosamente *****\n")
        self.guardar_base_de_datos()

    def iniciar_sesion(self):
        nombre = input("Ingrese su nombre de usuario: ")
        contrasenia = input("Ingrese su contraseña: ")

        for usuario in self.base_de_datos:
            if f"Nombre : {nombre}" in usuario and f"Contraseña : {contrasenia}" in usuario:
                print(f"\n***** Bienvenido {nombre} *****\n")
                return
        print("\n!!! Usuario o contraseña incorrectos !!!\n")

    def mostrar_usuarios(self):
        print("*** Los usuarios registrados son: ***\n")
        for usuario in self.base_de_datos:
            print(usuario.split(" | ")[0][10:])
        print("\n *** Fin de la lista de usuarios *** \n")