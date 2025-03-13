class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """Invierte el orden de los elementos en una lista manualmente."""
        resultado = []
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado
    
        pass
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1 


    pass
    
    def eliminar_duplicados(self, lista):
        """Elimina elementos duplicados de una lista manteniendo el orden."""
        resultado = []
        vistos = {}
        for item in lista:
            if item not in vistos:
                resultado.append(item)
                vistos[item] = True
        return resultado
    
        pass
    
    def merge_ordenado(self, lista1, lista2):
        """Combina dos listas ordenadas en una sola lista ordenada."""
        resultado = []
        i, j = 0, 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
        pass
    
    def rotar_lista(self, lista, k):
        """Rota los elementos de una lista k posiciones a la derecha."""
        k %= len(lista)
        return lista[-k:] + lista[:-k]
        pass
    
    def encuentra_numero_faltante(self, lista):
        """Encuentra el número faltante en una lista de enteros del 1 al n."""
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        return suma_esperada - suma_real
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """Verifica si conjunto1 es subconjunto de conjunto2."""
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
        
        pass
    
    def implementar_pila(self):
        """Implementa una pila usando listas con métodos push, pop, peek y is_empty."""
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }
        pass
    
    def implementar_cola(self):
        """Implementa una cola usando listas con métodos enqueue, dequeue, peek y is_empty."""
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0) if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }

        pass
    
    
        if not matriz or not matriz[0]:
            return []
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    pass