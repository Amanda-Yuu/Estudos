idade = int(input("Digite um número: "))

if idade % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 18:
    print("Você é um adolescente.")
elif idade > 18:
    print("Você é um adulto.")
else:
    print("Idade inválida.")

nome = int(input("Digite seu nome: "))
senha = int(input("Digite sua senha: "))
usuario_esperado = nome
senha_esperada = senha

usuario = input("Digite o nome de usuário: ") and senha = input("Digite a senha: ")

if usuario == usuario_esperado and senha == senha_esperada:
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")

