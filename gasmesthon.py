#Projeto Curso Logica de Programação -- Catálogo de Jogos
from crud_clientes import consultar_clientes, cadastrar_cliente
from crud_games import adicionar_jogo, consultar_jogos, remover_jogo, atualizar_jogo
  
jogo_catalogo = []
clientes_lista = []

#Variável de controle das opções do usuário
opt = 0
while opt != 10:
  # Menu do usuário
  print('''
  \033[32m***************************\033[m
  \033[32m*\033[34mCATALOGO_DE_GAMES_C-JOVEM\033[32m*\033[m
  \033[32m***************************\033[m
  [ 1 ] Adicionar Novo Jogo
  [ 2 ] Cadastrar Novo Cliente
  [ 3 ] Alugar Jogo
  [ 4 ] Consultar Catálogo de Jogos
  [ 5 ] Consultar Lista de Clientes
  [ 6 ] Atualizar Registro de Jogos
  [ 7 ] Atualizar Registro de Clientes
  [ 8 ] Deletar Jogo do Catálogo
  [ 9 ] Cancelar Cadastro do Cliente  
  [ 10 ] Sair
  ''')
  opt = int(input("Digite a sua opção: "))

  match opt:
    case 1:
      print('''
************************
*CADASTRO DE NOVOS JOGO*
************************
      ''')
      jogo_catalogo.append(adicionar_jogo())
      print('\033[32mJogo cadastrado com sucesso!\033[m')

    case 2:
        print('''
**********************
*CADASTRO DE CLIENTES*
**********************
      ''')
        clientes_lista.append(cadastrar_cliente())
        print('\033[32mCliente Cadastrado com sucesso!\033[m')

    case 4:
        print('''
**************************
*   CATALOGO DE JOGOS    * 
************************** 
        ''')
        read_opt = 0
        while read_opt != 6:
            print('''[ 1 ] Vizualizar Catalogo Completo\n[ 2 ] Consultar por nome\n[ 3 ] Consultar por categoria\n[ 4 ] Consultar por ano de lançamento\n[ 5 ] Consultar por plataforma\n[ 6 ] Sair
            ''')
            read_opt = int(input('Digite sua opção: '))
            match read_opt:
                case 1:
                    consultar_jogos(jogo_catalogo)
                case 2:
                    nome = input("Digite o nome: ")
                    consultar_jogos(jogo_catalogo, nome=nome)
                case 3:
                    cat = input("Digite a categoria: ")
                    consultar_jogos(jogo_catalogo, categoria=cat)
                case 4:
                    ano = input("Digite o ano de lançamento: ")
                    consultar_jogos(jogo_catalogo, ano=ano)
                case 5:
                    platf = input("Digite a plataforma: ")
                    consultar_jogos(jogo_catalogo, plataforma=platf)        

        

    case 6:
        print('''
*******************************
* ATUALIZANDO REGISTROS (JOGO)*
*******************************    
''')
        user_opt = 0
        while user_opt != 6:
           print('''[ 1 ] Atualizar registro completo\n[ 2 ] Atualizar apenas nome\n[ 3 ] Atualizar apenas categoria\n[ 4 ]Atualizar apenas ano de lançamento\n[ 5 ] Atualizar apenas plataforma\n[ 6 ] Sair\n''')
           user_opt = int(input('Digite a opcao: '))
           match user_opt:
              case 1:
                 index = int(input("Digite o indice do jogo(caso necessário volte no menu principal e use a funcao consultar jogos): "))
                 atualizar_jogo(jogo_catalogo, index)
              case 2:
                 index = int(input("Digite o indice do jogo(caso necessário volte no menu principal e use a funcao consultar jogos): "))
                 atualizar_jogo(jogo_catalogo, index, nome=True)
              case 3:
                 index = int(input("Digite o indice do jogo(caso necessário volte no menu principal e use a funcao consultar jogos): "))
                 atualizar_jogo(jogo_catalogo, index, categoria=True)
              case 4:
                 index = int(input("Digite o indice do jogo(caso necessário volte no menu principal e use a funcao consultar jogos): "))
                 atualizar_jogo(jogo_catalogo, index, ano=True)
              case 5:
                 index = int(input("Digite o indice do jogo(caso necessário volte no menu principal e use a funcao consultar jogos): "))
                 atualizar_jogo(jogo_catalogo, index, plataforma=True)


    case 8:
      print('''
**************************
*                        *
**************************
      ''')
      jogo_index = int(input("Insira o indice do jogo que deseja deletar: "))
      remover_jogo(jogo_index, jogo_catalogo)
      print('\033[33mJogo removido com sucesso!\033[m')

    case 5:
      print('''
************************
*   LISTA DE CLIENTES   *
************************
        ''')
      consultar_clientes(clientes_lista)


print("\033[33m TCHAU, VOLTE SEMPRE!!!\033[m")