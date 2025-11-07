renda= float(input("Qual o valor da sua renda mensal?"))
parcela= int(input("Qual valor da parcelas deseja fazer? "))
porcentagem= 30

calculo_porcentagem= renda * (porcentagem / 100)

if renda > 2000.00 and parcela < calculo_porcentagem:
    print(f"Você esta apto para receber o emprestimo")
else:
    print("Você não está apto para receber o empresimo")