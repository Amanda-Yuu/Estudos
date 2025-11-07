nota1= float(input("digite a nota do aluno: "))
nota2= float(input("digite a nota do aluno: "))
nota3= float(input("digite a nota do aluno: "))

media= (nota1 + nota2 + nota3) /3
if media >=8:
    print("Aluno(a) aprovado!")
elif 5<= media < 7:
    print("Aluno(a) recuperação")
elif media <5:
    print("Aluno(a) reprovado.")