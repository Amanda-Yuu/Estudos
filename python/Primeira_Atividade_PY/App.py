import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. alternar estado do restaurantes')
    print('4. Encerrando o programa')

def finalizar_app ():
    os.system('cls')
    # os.system('clear')
    print('Finalizando app')

def voltar_ao_menu_principal():
    input('\nAperte uma tecla para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print ('Opção invalida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos resurantes')
    nome_do_restaurante = input('Digite o nome do restaurente que deseja cadastrar: ')
    categoria = input ('Digite a categoria do seu restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,
    'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes\n')

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
        print(f' -{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input ('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

def escolher_opcao():
    try:
            opcao_escolhida = int (input('escolha uma opção: '))
            # opcao_escolhida = int (opcao_escolhida)
            if opcao_escolhida == 1:
                cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                listar_restaurantes()
            elif opcao_escolhida == 3:
                alternar_estado_do_restaurante()
            elif opcao_escolhida ==4:
                finalizar_app();
            else:
                opcao_invalida()
    except ValueError:
        opcao_invalida()

#opcao_escolhida = input('Escolha uma opação:');
#print (f'Você escolheu a opção {opcao_escolhida}');

def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()