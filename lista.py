from nodo import Node


class ListaEnlazada:
    def __init__(self):
        self.head = None

    def __str__(self):
        elementos = []
        current = self.head
        while current:
            elementos.append(str(current.valor) + " |")
            current = current.next
        return " ".join(elementos)

    def add_node(self, valor):
        new_node = Node(valor)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def obtenerNodos(self):
        # La lista tiene elementos
        aux = self.head
        NodoTexto = ""

        # Creando Nodos
        NodoTexto += "\n"
        NodoTexto += "\n"
        while aux is not None:
            color = ""
            if aux.valor == "A" or aux.valor == "a":
                color = "blue"
            elif aux.valor == "R" or aux.valor == "r":
                color = "red"
            elif aux.valor == "V" or aux.valor == "V":
                color = "green"
            elif aux.valor == "P" or aux.valor == "p":
                color = "purple"
            elif aux.valor == "N" or aux.valor == "n":
                color = "orange"
            NodoTexto += (
                "node"
                + str(id(aux))
                + ' [style=filled, fillcolor="'
                + color
                + '", shape=oval, label=" '
                + str(aux.valor)
                + '  "]\n'
            )
            aux = aux.next
        NodoTexto += "\n"
        NodoTexto += "\n"

        # Enlazando Nodos
        aux = self.head
        while aux.next is not None:
            NodoTexto += "node" + str(id(aux)) + " -> node" + str(id(aux.next)) + "\n"
            aux = aux.next

        idcabeza = id(self.head)
        return [NodoTexto, idcabeza]

    def modify_by_index(self, indice, nuevo_valor):
        if indice < 0:
            raise ValueError("El índice no puede ser negativo")

        current = self.head
        posicion_actual = 0

        while current:
            if posicion_actual == indice:
                current.valor = nuevo_valor
                return
            current = current.next
            posicion_actual += 1

        raise IndexError("El índice está fuera de rango")

    def display(self):
        current = self.head
        while current:
            print(current.valor)
            current = current.next

    def clear(self):
        self.head = None

    def get_by_index(self, index):
        if index < 0:
            raise ValueError("El índice no puede ser negativo")

        current = self.head
        posicion_actual = 0

        while current:
            if posicion_actual == index:
                return current.valor
            current = current.next
            posicion_actual += 1

        raise IndexError("El índice está fuera de rango")
