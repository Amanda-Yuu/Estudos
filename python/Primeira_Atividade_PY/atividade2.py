numeros = list (range(1,11))
nomes = [{'gabriel', 'Carlos', 'erick', 'giovanna'}]
anos = list (range(2000, 2026))

numero_escolhido = int(input('Escolha um numero de 1 a 10: '))
for numero_tabuada in range (1, 11):
    print(f' {numero_escolhido} X {numero_tabuada} = {numero_escolhido*numero_tabuada}')

soma_impares = 0
for numeros in range (1, 11, 2): #o argumento 2 faz com que o loop pule os numeros pares
    soma_impares +=numeros
    print (soma_impares)

numeros_descrescente = -1
for numeros_descrescente in range (10 , 0, -1):
    print (numeros_descrescente)


for anos in range (2000, 2026):
    print (anos)


for nome in nomes:
    print(nome)
