# altura= []
# peso= []
# imc=[]

# print("Vamos qualquelar seu IMC")
# numeroAltura = float(input("Qual é sua altura? "))
# altura.append(numeroAltura)
# numeroPeso = int(input("Qual seu Kg? "))
# peso.append(numeroPeso)

# Calculo_IMC= peso/(altura ** 2) = imc
# imc.append(Calculo_IMC)

# print(imc)

print("Vamos calcular seu IMC")
altura= float(input("Digite a sua altura: "))
peso= int(input("Digite seu peso em KG: "))

calculo_imc= peso/(altura **2)

print(f"Seu IMC é: {calculo_imc:.2f}")

if calculo_imc < 18.5:
    print("Você esta a baixo do peso")

elif calculo_imc >= 25:
    print("A cima do peso")

else:
    print("Peso ok")