class Registro:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, calificaciones):
        self.estudiantes[nombre] = calificaciones

    def buscar_estudiante(self, nombre):
        return self.estudiantes.get(nombre, "El estudiante no esta registrado")

    def actualizar_calificaciones(self, nombre, calificaciones):
        if nombre in self.estudiantes:
            self.estudiantes[nombre] = calificaciones
            return True
        return False

    def eliminar_estudiante(self, nombre):
        if nombre in self.estudiantes:
            del self.estudiantes[nombre]
            return True
        return False

    def mostrar_estudiantes(self):
        return self.estudiantes


def main():
    registro = Registro()
    while True:
        print("1. Agregar estudiante")
        print("2. Buscar estudiante")
        print("3. Actualizar calificaciones")
        print("4. Eliminar estudiante")
        print("5. Mostrar todos los estudiantes")
        print("6. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            nombre = input("Nombre del estudiante: ")
            calificaciones = list(map(int, input("Calificaciones (separadas por espacios): ").split()))
            registro.agregar_estudiante(nombre, calificaciones)
        elif opcion == 2:
            nombre = input("Nombre del estudiante: ")
            print(registro.buscar_estudiante(nombre))
        elif opcion == 3:
            nombre = input("Nombre del estudiante: ")
            calificaciones = list(map(int, input("Nuevas calificaciones (separadas por espacios): ").split()))
            registro.actualizar_calificaciones(nombre, calificaciones)
        elif opcion == 4:
            nombre = input("Nombre del estudiante: ")
            registro.eliminar_estudiante(nombre)
        elif opcion == 5:
            print(registro.mostrar_estudiantes())
        elif opcion == 6:
            break


if __name__ == "__main__":
    main()
