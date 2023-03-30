class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.buckets = [None] * capacidad
        
    def hash_func(hash, clave):
        return hash(clave) % hash.capacidad
        
    def insertar(hash, clave, valor):
        indice = hash.hash_func(clave)
        
        if hash.buckets[indice] is None:
            hash.buckets[indice] = Nodo(clave, valor)
        else:
            actual = hash.buckets[indice]
            while actual.siguiente is not None and actual.clave != clave:
                actual = actual.siguiente
            if actual.clave == clave:
                actual.valor = valor
            else:
                actual.siguiente = Nodo(clave, valor)
                
    def buscar(hash, clave):
        indice = hash.hash_func(clave)
        actual = hash.buckets[indice]
        while actual is not None:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente
        raise KeyError('Clave no encontrada')
    
#encriptar 1 caracter a 8 caracteres, se haran dos encriptaciones por tablas hash para encriptar y desencriptar, con los carcateres del 32 al 125 de la tabla ASCII

    def encriptar(hash):
        cadena = input("Ingrese la cadena a encriptar: ")
        cadena_encriptada = ""
        for i in range(len(cadena)):
            indice = hash.hash_func(cadena[i])
            actual = hash.buckets[indice]
            while actual is not None:
                if actual.clave == cadena[i]:
                    cadena_encriptada += actual.valor
                actual = actual.siguiente
        print("Cadena encriptada: " + cadena_encriptada)
    
    def desencriptar(hash):
        cadena = input("Ingrese la cadena a desencriptar: ")
        cadena_desencriptada = ""
        for i in range(len(cadena)):
            indice = hash.hash_func(cadena[i])
            actual = hash.buckets[indice]
            while actual is not None:
                if actual.clave == cadena[i]:
                    cadena_desencriptada += actual.valor
                actual = actual.siguiente
        print("Cadena desencriptada: " + cadena_desencriptada)