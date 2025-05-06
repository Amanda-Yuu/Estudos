from abc import ABC, ABC, abstractclassmethod


class Item_cardapio(ABC):
    def __init__ (self, nome, preco):
        self._nome = nome
        self._preco = preco


    @abstractclassmethod
    def aplicar_desconto(self):
        pass