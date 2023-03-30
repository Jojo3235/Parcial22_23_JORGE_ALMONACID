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
    
def main():  
    alumno1 = Alumno("Juan", 6)
    alumno2 = Alumno("Pedro", 4)
    alumno3 = Alumno("Maria", 7)
    alumno4 = Alumno("Ana", 3)
    print(alumno1)
    print(alumno2)
    print(alumno3)
    print(alumno4)

if __name__ == "__main__":
    main()