class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada(object):
    def __init__(self):
        self.cabeza = None

    def agregar(lista, valor):
        nodo_nuevo = Nodo(valor)
        if lista.cabeza is None:
            lista.cabeza = nodo_nuevo
        else:
            nodo_actual = lista.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo

    def get(lista, index):
        nodo_actual = lista.cabeza
        for i in range(index):
            nodo_actual = nodo_actual.siguiente
        return nodo_actual.valor
    
    def set(lista, index, valor):
        nodo_actual = lista.cabeza
        for i in range(index):
            nodo_actual = nodo_actual.siguiente
        nodo_actual.valor = valor

    def remove(lista, index):
        if index == 0:
            lista.cabeza = lista.cabeza.siguiente
        else:
            nodo_actual = lista.cabeza
            for i in range(index - 1):
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_actual.siguiente.siguiente

    def size(lista):
        nodo_actual = lista.cabeza
        size = 0
        while nodo_actual is not None:
            size += 1
            nodo_actual = nodo_actual.siguiente
        return size
    
    def __str__(self):
        nodo_actual = self.cabeza
        cadena = ""
        while nodo_actual is not None:
            cadena += str(nodo_actual.valor) + " "
            nodo_actual = nodo_actual.siguiente
        return cadena
    
class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = []
        for i in range(m):
            row = ListaEnlazada()
            for j in range(n):
                row.agregar(None)
            self.matrix.append(row)

    def set_value(matrix, i, j, value):
        matrix.matrix[i].set(j, value)

    def get_value(matrix, i, j):
        return matrix.matrix[i].get(j)

    def print_matrix(matrix):
        for i in range(matrix.m):
            row = ''
            for j in range(matrix.n):
                row += str(matrix.get_value(i, j)) + ' '
            print(row)
    
    def determinante_iterativo(matrix):
        if matrix.m != matrix.n:
            raise ValueError("La matriz debe ser cuadrada")
        if matrix.m == 1:
            return matrix.get_value(0, 0)
        if matrix.m == 2:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0)
        if matrix.m == 3:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) * matrix.get_value(2, 2) + matrix.get_value(0, 1) * matrix.get_value(1, 2) * matrix.get_value(2, 0) + matrix.get_value(0, 2) * matrix.get_value(1, 0) * matrix.get_value(2, 1) - matrix.get_value(0, 2) * matrix.get_value(1, 1) * matrix.get_value(2, 0) - matrix.get_value(0, 0) * matrix.get_value(1, 2) * matrix.get_value(2, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0) * matrix.get_value(2, 2)
        else:
            determinante = 0
            for i in range(matrix.m):
                determinante += (-1) ** i * matrix.get_value(0, i) * matrix.cofactor(0, i).determinante_iterativo()
            return determinante

    def cofactor(matrix, i, j):
        cofactor = Matrix(matrix.m - 1, matrix.n - 1)
        for k in range(cofactor.m):
            for l in range(cofactor.n):
                if k < i and l < j:
                    cofactor.set_value(k, l, matrix.get_value(k, l))
                elif k < i and l >= j:
                    cofactor.set_value(k, l, matrix.get_value(k, l + 1))
                elif k >= i and l < j:
                    cofactor.set_value(k, l, matrix.get_value(k + 1, l))
                elif k >= i and l >= j:
                    cofactor.set_value(k, l, matrix.get_value(k + 1, l + 1))
        return cofactor

    def strassen_determinante(matrix):
        if matrix.m != matrix.n:
            raise ValueError("La matriz debe ser cuadrada")
        if matrix.m == 1:
            return matrix.get_value(0, 0)
        if matrix.m == 2:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0)
        if matrix.m == 3:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) * matrix.get_value(2, 2) + matrix.get_value(0, 1) * matrix.get_value(1, 2) * matrix.get_value(2, 0) + matrix.get_value(0, 2) * matrix.get_value(1, 0) * matrix.get_value(2, 1) - matrix.get_value(0, 2) * matrix.get_value(1, 1) * matrix.get_value(2, 0) - matrix.get_value(0, 0) * matrix.get_value(1, 2) * matrix.get_value(2, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0) * matrix.get_value(2, 2)
        else:
            a = Matrix(matrix.m // 2, matrix.n // 2)
            b = Matrix(matrix.m // 2, matrix.n // 2)
            c = Matrix(matrix.m // 2, matrix.n // 2)
            d = Matrix(matrix.m // 2, matrix.n // 2)
            for i in range(matrix.m // 2):
                for j in range(matrix.n // 2):
                    a.set_value(i, j, matrix.get_value(i, j))
                    b.set_value(i, j, matrix.get_value(i, j + matrix.n // 2))
                    c.set_value(i, j, matrix.get_value(i + matrix.m // 2, j))
                    d.set_value(i, j, matrix.get_value(i + matrix.m // 2, j + matrix.n // 2))
            p1 = Matrix.strassen_determinante(a)
            p2 = Matrix.strassen_determinante(b)
            p3 = Matrix.strassen_determinante(c)
            p4 = Matrix.strassen_determinante(d)
            return p1 * p4 - p2 * p3
        
def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Debe ingresar un número")

def main():
    matrix = Matrix(5,5)
    for i in range(5):
        for j in range(5):
            matrix.set_value(i, j, pedir_numero())
    print("La matriz es:")
    matrix.print_matrix()
    print("El determinante de la matriz de manera iterativa es:", Matrix.determinante_iterativo(matrix))
    print("El determinante de la matriz de manera recursiva es:", Matrix.strassen_determinante(matrix))
    

if __name__ == "__main__":
    main()