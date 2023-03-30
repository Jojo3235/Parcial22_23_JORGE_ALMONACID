class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado con éxito")

    def calificacion(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Suspendido"


def main():  
    alumno1 = Alumno("Juan", 6)
    alumno2 = Alumno("Pedro", 4)
    alumno3 = Alumno("Maria", 7)
    alumno4 = Alumno("Ana", 3)
    print(alumno1.calificacion())
    print(alumno2.calificacion())
    print(alumno3.calificacion())
    print(alumno4.calificacion())

if __name__ == "__main__":
    main()