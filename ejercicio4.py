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

    def __str__(self):
        return self.nombre + " " + str(self.nota)