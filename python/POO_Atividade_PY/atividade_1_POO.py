'''Em uma carreira de desenvolvimento de software, a prática 
consistente desempenha um papel fundamental na construção de bases sólidas. 
Pensando nisso, criamos uma lista de atividades (não obrigatórias) 
focada em prática para melhorar ainda mais sua experiência de aprendizagem.

Bora praticar então?


Exercícios
1 - Implemente uma classe chamada Carro com os atributos básicos, 
como modelo, cor e ano. Crie uma instância dessa classe e atribua valores 
aos seus atributos. 

2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, 
ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores 
aos seus atributos.

3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e 
categoria como parâmetros e inicia ativo como False por padrão. Crie uma 
instância utilizando o construtor.

4 - Adicione um método especial __str__ à classe Restaurante para que, ao 
imprimir uma instância, seja exibida uma mensagem formatada com o nome e a 
categoria. Exiba essa mensagem para uma instância de restaurante.

5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, 
instancie 3 objetos desta classe e atribua valores aos seus atributos 
através de um método construtor.'''

class Carro:
    def __init__(self, cor, ano, modelo):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo


class Restaurante:
    def __init__(self, nome, categoria, ativo=false, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __star__(self):
    # `__str__` para que exiba essa mensagem para uma instância de restaurante.
        return f'{self.nome} | {self.categoria}'
    

# Instanciando um restaurante e atribuindo valores aos seus atributos
meu_restaurante = Restaurante(nome='Comida boa', categoria='gourmet', ativo=True, capacidade=50, nota_avaliacao=4.5)
print(meu_restaurante)

class Cliente>
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')