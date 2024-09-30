#Função para registrar cliente
def cadastrar_cliente():
  validez = False
  while validez != True:
    cliente = {
        'nome': input("Insira o nome do cliente: "),
        'endereco' : input("Insira o endereço: "),
        'email': input("Insira o email do cliente: "),
        'senha' : input("Digite a senha: ")
              }
    validez = confirmar_senha(cliente['senha'])
    return cliente

#Função para validar a senha
def confirmar_senha(senha):
  verify = False
  while verify != True:
    confirmacao = input("Confirmar a senha: ")
    if confirmacao == senha:
      verify = True
      return verify
    else:
      print('\033[31mSenha inválida!\033[m')

#Função para consultar clientes
def consultar_clientes(database):
  index = 0
  for i in database:
        cliente = i.items()
        print(f'INDICE : {index}')
        for j in cliente:
            print(f'{j[0].upper()} : {j[1].lower()}')
        print('--------------------------')
        index += 1