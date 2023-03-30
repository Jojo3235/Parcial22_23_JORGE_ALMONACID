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
    
    def buscar(lista, valor, maximo):
        nodo_actual = lista.cabeza
        for i in range(maximo):
            if nodo_actual.valor == valor:
                return i
            nodo_actual = nodo_actual.siguiente
        return -1
    
    def buscar_multiplo(lista, valor, maximo):
        nodo_actual = lista.cabeza
        for i in range(maximo):
            if nodo_actual.valor % valor == 0:
                return i
            nodo_actual = nodo_actual.siguiente
        return -1

    def devolver_lista_hasta(lista, maximo):
        nodo_actual = lista.cabeza
        for i in range(maximo):
            if nodo_actual.valor > maximo:
                return i
            nodo_actual = nodo_actual.siguiente
        return -1
    
    def devolver_indices(lista, valor):
        nodo_actual = lista.cabeza
        indices = ListaEnlazada()
        i = 0
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                indices.agregar(i)
            nodo_actual = nodo_actual.siguiente
            i += 1
        return indices
    
    def merge(lista1, lista2):
        lista3 = ListaEnlazada()
        nodo_actual = lista1.cabeza
        while nodo_actual is not None:
            lista3.agregar(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        nodo_actual = lista2.cabeza
        while nodo_actual is not None:
            lista3.agregar(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return lista3

    def mergesort(lista):
        if lista.size() > 1:
            mitad = lista.size() // 2
            lista1 = ListaEnlazada()
            lista2 = ListaEnlazada()
            for i in range(mitad):
                lista1.agregar(lista.get(i))
            for i in range(mitad, lista.size()):
                lista2.agregar(lista.get(i))
            lista1 = ListaEnlazada.mergesort(lista1)
            lista2 = ListaEnlazada.mergesort(lista2)
            lista = ListaEnlazada.merge(lista1, lista2)
        return lista

    def __str__(lista):
        nodo_actual = lista.cabeza
        cadena = ""
        while nodo_actual is not None:
            cadena += str(nodo_actual.valor) + " -> "
            nodo_actual = nodo_actual.siguiente
        return cadena
    
def main():
    lista = ListaEnlazada()
    lista.agregar(18)
    lista.agregar(50)
    lista.agregar(210)
    lista.agregar(80)
    lista.agregar(145)
    lista.agregar(333)
    lista.agregar(70)
    lista.agregar(30)
    print("Imprimir nuemero si es multiplo de 10 menor que 200")
    print(lista.buscar_multiplo(10, lista.size()))
    print("Busqueda hasta 300")
    print(lista.devolver_lista_hasta(300))
    print("Ordenar lista")
    # print(lista.mergesort(lista))
    print("Indice de 145")
    print(lista.devolver_indices(145))

if __name__ == "__main__":
    main()