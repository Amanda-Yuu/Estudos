import os

restaurantes = []


def exibir_nome_do_programa():
    print('Sabor Express\n');

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Encerrando o programa')

def finalizar_app ():
    os.system('cls')
    # os.system('clear')
    print('Finalizando app')

def opcao_invalida():
    print ('Opção invalida\n')
    input('Aperte uma tecla para volta ao menu principal');
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos resurantes')
    nome_dorestaurante = input('Digite o nome do restaurente que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_dorestaurante} foi cadastrado com sucesso!')
    input('Aperte uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
            opcao_escolhida = int (input('escolha uma opção: '));
            # opcao_escolhida = int (opcao_escolhida)
            if opcao_escolhida == 1:
                print('Cadastrar restaurante')
            elif opcao_escolhida == 2:
                print('Listar restaurantes')
            elif opcao_escolhida == 3:
                print('Ativar restaurantes')
            elif opcao_escolhida ==4:
                finalizar_app();
            else:
                opcao_invalida
    except:
        opcao_invalida

#opcao_escolhida = input('Escolha uma opação:');
#print (f'Você escolheu a opção {opcao_escolhida}');

def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()