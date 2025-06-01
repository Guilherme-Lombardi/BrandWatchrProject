# utils/lista_encadeada.py

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self._tamanho = 0

    def inserir(self, node: Node):
        if not self.inicio:
            self.inicio = node
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = node
        self._tamanho += 1

    def para_lista(self) -> list:
        dados = []
        atual = self.inicio
        while atual:
            dados.append(atual.dado)
            atual = atual.proximo
        return dados

    def __len__(self):
        return self._tamanho
