import sys 
sys.path.insert(0, 'ej3')
import unittest
from ejercicio3 import Alumno

class TestAlumno(unittest.TestCase):
        
        def test_agregar_notas(self):
            alumno1 = Alumno("Juan", 10)
            alumno2 = Alumno("Pedro", 3)
            self.assertEqual(alumno1.calificacion(), "Aprobado")
            self.assertEqual(alumno2.calificacion(), "Suspendido")
