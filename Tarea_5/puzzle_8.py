import random
from collections import deque

class Tablero:
    OBJETIVO = ((1, 2, 3), (4, 5, 6), (7, 8, 0)) # Objetivo del puzzle 
    MOVIMIENTOS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
    
    def __init__(self, estado=None):
        self.estado = estado if estado else self.generar_estado()
    
    @staticmethod
    def generar_estado():
        numeros = list(range(9))
        random.shuffle(numeros)
        return tuple(tuple(numeros[i:i+3]) for i in range(0, 9, 3))
    
    def encontrar_vacio(self):
        for i, fila in enumerate(self.estado):
            for j, valor in enumerate(fila):
                if valor == 0:
                    return i, j
    
    def es_resoluble(self):
        plano = sum(self.estado, ())
        desorden_total = sum(1 for i in range(len(plano)) for j in range(i + 1, len(plano)) 
                            if plano[i] and plano[j] and plano[i] > plano[j])
        return desorden_total % 2 == 0
    
    def obtener_vecinos(self):
        x_vacio, y_vacio = self.encontrar_vacio()
        vecinos = []
        
        for dx, dy in self.MOVIMIENTOS:
            nuevo_x, nuevo_y = x_vacio + dx, y_vacio + dy
            if 0 <= nuevo_x < 3 and 0 <= nuevo_y < 3:
                nuevo_estado = [list(fila) for fila in self.estado]
                nuevo_estado[x_vacio][y_vacio], nuevo_estado[nuevo_x][nuevo_y] = \
                    nuevo_estado[nuevo_x][nuevo_y], nuevo_estado[x_vacio][y_vacio]
                vecinos.append((tuple(tuple(fila) for fila in nuevo_estado), (x_vacio, y_vacio), (nuevo_x, nuevo_y)))
        
        return vecinos
    
    def imprimir(self):
        for fila in self.estado:
            print(fila)
        print()
    
    def esta_resuelto(self):
        return self.estado == self.OBJETIVO

class ResolverPuzzle:
    def __init__(self, tablero):
        self.tablero = tablero
    
    def resolver(self):
        if not self.tablero.es_resoluble():
            return None
        
        cola = deque([(self.tablero.estado, [], None)])
        visitados = {self.tablero.estado}
        
        while cola:
            estado, camino, _ = cola.popleft()
            
            if estado == Tablero.OBJETIVO:
                return camino
            
            for vecino, pos_vacio, nueva_pos in Tablero(estado).obtener_vecinos():
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [(pos_vacio, nueva_pos)], pos_vacio))
        
        return None
    
    def mostrar_solucion(self, solucion):
        if solucion is None:
            print("No se pudo resolver el puzzle. El estado inicial no es resoluble.")
            return
        
        print("Tablero inicial:")
        self.tablero.imprimir()
        estado_actual = self.tablero.estado
        
        for mov in solucion:
            vacio, nuevo = mov
            x_vacio, y_vacio = vacio
            x_nuevo, y_nuevo = nuevo
            nuevo_estado = [list(fila) for fila in estado_actual]
            nuevo_estado[x_vacio][y_vacio], nuevo_estado[x_nuevo][y_nuevo] = nuevo_estado[x_nuevo][y_nuevo], nuevo_estado[x_vacio][y_vacio]
            estado_actual = tuple(tuple(fila) for fila in nuevo_estado)
            print(f"Moviendo vacío de {vacio} a {nuevo}:")
            for fila in estado_actual:
                print(fila)
            print()
        
        print("Tablero resuelto:")
        for fila in Tablero.OBJETIVO:
            print(fila)

if __name__ == "__main__":
    tablero_inicial = Tablero()
    solucionador = ResolverPuzzle(tablero_inicial)
    solucion = solucionador.resolver()
    solucionador.mostrar_solucion(solucion)
