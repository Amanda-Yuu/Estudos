class Restaurante:
    #self é uma propriedade dentro de uma classe
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

        #__str__ é usado para mostrar as info em sting 
    def __str__(self): 
        return f'{self.nome} | {self.categoria}'
        
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)