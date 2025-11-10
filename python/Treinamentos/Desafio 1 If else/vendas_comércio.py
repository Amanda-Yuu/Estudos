#macas= 15
#bananas= 30

frutas=["macas", "bananas", "maracuja", "abacaxi"]
quantidade_frutas =[]
for items in frutas:
    #print(frutas)
    quantidade = int(input (f"Quanto de {items} foi vendido? "))
    quantidade_frutas.append(quantidade)

if quantidade_frutas[0] > quantidade_frutas [1] and quantidade_frutas[0] > quantidade_frutas[2] and quantidade_frutas[0] > quantidade_frutas[3]:
    print(f"{frutas[0]} foi mais vendido")

elif quantidade_frutas[1] > quantidade_frutas [0] and quantidade_frutas[1] > quantidade_frutas[2] and quantidade_frutas[1] > quantidade_frutas[3]:
    print(f"{frutas[1]} foi mais vendido")

elif quantidade_frutas[2] > quantidade_frutas [0] and quantidade_frutas[2] > quantidade_frutas[1] and quantidade_frutas[2] > quantidade_frutas[3]:
    print(f"{frutas[2]} foi mais vendido")

elif quantidade_frutas[3] > quantidade_frutas [0] and quantidade_frutas[3] > quantidade_frutas[1] and quantidade_frutas[3] > quantidade_frutas[2]:
    print(f"{frutas[3]} foi mais vendido")

