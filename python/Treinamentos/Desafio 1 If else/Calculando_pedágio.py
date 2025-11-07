kmPercorrido= float(input("Quantos km percorridos?"))

if kmPercorrido >= 100:
    print("Valor do pedágio: R$10,00")
elif 100< kmPercorrido <=200:
    print("valor do pedágio: R$20,00")
elif kmPercorrido>200:
    print("valor do pedágio: R$30,00")