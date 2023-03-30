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
        # Función hash básica que devuelve el índice de un bucket
        # basado en la clave, en este caso simplemente el módulo
        # de la longitud de la tabla hash.
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

    
def main():
    hash = TablaHash(100)
    hash.insertar(" ", "0")
    hash.insertar("!", "1")
    hash.insertar('"', "2")
    hash.insertar("#", "3")
    hash.insertar("$", "4")
    hash.insertar("%", "5")
    hash.insertar("&", "6")
    hash.insertar("'", "7")
    hash.insertar("(", "8")
    hash.insertar(")", "9")
    hash.insertar("*", "10")
    hash.insertar("+", "11")
    hash.insertar(",", "12")
    hash.insertar("-", "13")
    hash.insertar(".", "14")
    hash.insertar("/", "15")
    hash.insertar("0", "16")
    hash.insertar("1", "17")
    hash.insertar("2", "18")
    hash.insertar("3", "19")
    hash.insertar("4", "20")
    hash.insertar("5", "21")
    hash.insertar("6", "22")
    hash.insertar("7", "23")
    hash.insertar("8", "24")
    hash.insertar("9", "25")
    hash.insertar(":", "26")
    hash.insertar(";", "27")
    hash.insertar("<", "28")
    hash.insertar("=", "29")
    hash.insertar(">", "30")
    hash.insertar("?", "31")
    hash.insertar("@", "32")
    hash.insertar("A", "33")
    hash.insertar("B", "34")
    hash.insertar("C", "35")
    hash.insertar("D", "36")
    hash.insertar("E", "37")
    hash.insertar("F", "38")
    hash.insertar("G", "39")
    hash.insertar("H", "40")
    hash.insertar("I", "41")
    hash.insertar("J", "42")
    hash.insertar("K", "43")
    hash.insertar("L", "44")
    hash.insertar("M", "45")
    hash.insertar("N", "46")
    hash.insertar("O", "47")
    hash.insertar("P", "48")
    hash.insertar("Q", "49")
    hash.insertar("R", "50")
    hash.insertar("S", "51")
    hash.insertar("T", "52")
    hash.insertar("U", "53")
    hash.insertar("V", "54")
    hash.insertar("W", "55")
    hash.insertar("X", "56")
    hash.insertar("Y", "57")
    hash.insertar("Z", "58")
    hash.insertar("[", "59")
    hash.insertar("\\", "60")
    hash.insertar("]", "61")
    hash.insertar("^", "62")
    hash.insertar("_", "63")
    hash.insertar("`", "64")
    hash.insertar("a", "65")
    hash.insertar("b", "66")
    hash.insertar("c", "67")
    hash.insertar("d", "68")
    hash.insertar("e", "69")
    hash.insertar("f", "70")
    hash.insertar("g", "71")
    hash.insertar("h", "72")
    hash.insertar("i", "73")
    hash.insertar("j", "74")
    hash.insertar("k", "75")
    
