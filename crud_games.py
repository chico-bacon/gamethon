#Função para registrar jogo na lista
def adicionar_jogo():
  jogo = {
        'nome': input("Insira o nome: "),
        'ano': input("Insira ano de lançamento: "),
        'categoria': input("Insira a categoria: "),
        'plataforma': input('Insira a plataforma: '),
        'alugado':bool(False)
        }
  return jogo

#Função para remover jogo da lista
def remover_jogo(index, database):
  if index >= 0 and index <= len(database) - 1:
    database.remove(database[index])
  else:
     print('\033[31mJogo Não Encontrado!\033[m')

#Função para consultar jogos
def consultar_jogos(database, nome='', categoria='' ,plataforma='', ano=''):
  if len(database) == 0:
    print('\033[33mNão há jogos catalogados ainda!\033[m')
  else:
    for i in range(0, len(database)):
        if database[i]['nome'] == nome:
            print('--------------------------')
            print(f'INDICE : {i}')
            for j in database[i].items():
                print(f'{j[0].upper()} : {j[1]}')

        elif database[i]['categoria'] == categoria:
            print('--------------------------')
            print(f'INDICE : {i}')
            for j in database[i].items():
                print(f'{j[0].upper()} : {j[1]}') 

        elif database[i]['plataforma'] == plataforma:
            print('--------------------------')
            print(f'INDICE : {i}')
            for j in database[i].items():
                print(f'{j[0].upper()} : {j[1]}')  

        elif database[i]['ano'] == ano:
            print('--------------------------')
            print(f'INDICE : {i}')
            for j in database[i].items():
                print(f'{j[0].upper()} : {j[1]}')

        elif nome=='' and categoria=='' and ano=='' and plataforma=='':
            print(f'INDICE : {i}')
            for j in database[i].items():
                print(f'{j[0].upper()} : {j[1]}')
            print('--------------------------')   
 
#Função para atualizar registro do jogo
def atualizar_jogo(database, index ,nome=False, categoria=False ,plataforma=False, ano= False):
   if index <= 0 and index <= len(database) - 1:
    if nome == True:
        database[index]['nome'] = input('Atualizar nome: ')
    elif categoria == True:
        database[index]['categoria'] = input('Atualizar categoria: ')
    elif plataforma == True:
        database[index]['plataforma'] = input('Atualizar plataforma: ')
    elif ano == True:
        database[index]['ano'] = input('Lançamento atualizado: ')
    else:
        database[index]['nome'] = input('Atualizar nome: ')
        database[index]['categoria'] = input('Atualizar categoria: ')
        database[index]['plataforma'] = input('Atualizar plataforma: ')
        database[index]['ano'] = input('Lançamento atualizado: ')
   else:
      print('\033[31mJogo Não foi encontrado\033[m')
#Função de alugar jogo