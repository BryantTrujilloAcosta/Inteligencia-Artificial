class NodoArbol:
    #Metodo especial, en este caso lo utilizamos para no inicializar el constructor
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    #El _ es para hacer el metodo privado
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
        # Si el valor es igual al que pusiste, no hace nada por que no acepta duplicados

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def imprimir(self):
        self._imprimir_recursivo(self.raiz)
    #Metodo in order
    def _imprimir_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_recursivo(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._imprimir_recursivo(nodo.derecha)

# Llenamos el arbol para poder ver si el metodo imprimir sirve
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)

print("Árbol binario en orden:")
arbol.imprimir() 
#Buscando un numero que si esta para que regrese true
print("\nBuscando el valor 7:")
print(arbol.buscar(7)) 
#Buscando un numero que no esta para que regrese false
print("Buscando el valor 12:")
print(arbol.buscar(12)) 