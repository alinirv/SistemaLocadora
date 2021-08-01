from datetime import datetime
now = datetime.now()
#----------------------------------------------
def busca_qnt_modelo(veiculos_modelo):
  cont = 0
  acumulador =0
  memoria = 0
  j = 0
  while j < len(veiculos_modelo):
    for i in range (len(veiculos_modelo)):
      if veiculos_modelo[j] == veiculos_modelo[i]:
        cont = cont + 1
    if cont > acumulador:
      acumulador = cont
    if veiculos_modelo[j] != memoria:
      print('O modelo ',veiculos_modelo[j],'possui ',cont,'veiculos.')  
    cont =0
    memoria = veiculos_modelo[j] #memoria recebe a posição somente depois da 1 comparação
    j=j+1
#----------------------------------------------
def busca_modelo(veiculos_modelo):
  memoria = 0
  cont = 0
  acumulador =0
  j = 0
  while j < len(veiculos_modelo):
    for i in range (len(veiculos_modelo)):
     if veiculos_modelo[j] == veiculos_modelo[i]:
      cont = cont + 1
    if cont > acumulador:
      acumulador = cont
      memoria = veiculos_modelo[j]
    j=j+1
    cont=0
  return memoria
#-----------------------------------------------
def remover_item(lista, indice):
  i = indice
  while i < len(lista) - 1:
    lista[i] = lista[i + 1]
    i = i + 1
  lista.pop()
#-----------------------------------------------
def busca_verificar(lista, elem):
  i = 0
  while i < len(lista):
    if lista[i] == elem:
      return i
    i = i + 1
  return -1
#-----------------------------------------------
def busca_novo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  idade = 0
  memoria = 0
  ano_atual = now.year
  pos=0
  i =0
  while i < len(veiculos_ano):
    ano = int(veiculos_ano[i])
    idade = ano_atual - ano
    if memoria == 0:
      memoria = idade
    if idade < memoria:
      memoria = idade  
      pos=veiculos_ano[i] #se não comparar não recebe a posição
    i = i + 1
  for i in range(len(veiculos_ano)):
    if pos == veiculos_ano[i]:
      v_codigo = veiculos_codigo[i]
      v_modelo = veiculos_modelo[i]
      v_ano = veiculos_ano[i]
      print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))  
#-----------------------------------------------
def busca_velho(veiculos_codigo, veiculos_modelo, veiculos_ano):
  idade = 0
  memoria = 0
  ano_atual = now.year
  pos=0
  i =0
  while i < len(veiculos_ano):
    ano = int(veiculos_ano[i])
    idade = ano_atual - ano
    if memoria == 0:
      memoria = idade
    if idade > memoria:
      memoria = idade  
      pos=veiculos_ano[i] #se não comprar não recebe a posição
    i = i + 1
  for i in range(len(veiculos_ano)):
    if pos == veiculos_ano[i]:
      v_codigo = veiculos_codigo[i]
      v_modelo = veiculos_modelo[i]
      v_ano = veiculos_ano[i]
      print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))  
#-----------------------------------------------
def busca_ipva(veiculos_ano): 
  idade = 0
  memoria = 0
  quantidade = len(veiculos_ano)
  ano_atual = now.year
  i =0
  for i in range(len(veiculos_ano)):
    ano = int(veiculos_ano[i])
    idade = ano_atual - ano
    if idade > 20:
        memoria = memoria + 1
    
  if memoria != 0:
    porcentagem = (memoria / quantidade) * 100 
  return porcentagem # variavel não declarada se a memoria for = 0 ela não existe 
#-----------------------------------------------
def relatorio_ipva(veiculos_ano):
  ipva= busca_ipva(veiculos_ano)
  print('\n*** Relatorio Veiculo IPVA: ***')
  print ('{:.0f}% dos veiculos não pagam IPVA.'.format(ipva))
 #----------------------------------------------- 
def relatorio_veic_novo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  print('\n*** Relatorio Veiculos mais novo:  ***')
  busca_novo(veiculos_codigo, veiculos_modelo, veiculos_ano)  
#-----------------------------------------------
def relatorio_veic_velho(veiculos_codigo, veiculos_modelo, veiculos_ano):
  print('\n*** Relatorio Veiculos mais velho:  ***')
  busca_velho(veiculos_codigo, veiculos_modelo, veiculos_ano)  
#-----------------------------------------------
def relatorio_modelo_quantidade(veiculos_modelo):
  print('\n*** Relatorio Veiculos por modelo: ***')
  busca_qnt_modelo(veiculos_modelo)
#-----------------------------------------------
def relatorio_modelo(veiculos_modelo):
  modelo = busca_modelo(veiculos_modelo)
  print('\n*** Relatorio Veiculos por modelo: ***')
  print ('O modelo '+ str(modelo) +' é o que mais tem veiculos.')   
#----------------------------------------------
def relatorio_idade(cliente_nascimento):
  quantidade = len(cliente_nascimento)
  jovens = clientes_jovens(cliente_nascimento)
  adultos = clientes_adulto(cliente_nascimento)
  idoso = clientes_idoso(cliente_nascimento)
  print('\n*** Relatorio Clientes por idade ***')
  print ('\nQuantidade de Clientes:', quantidade)
  print ('{:.0f}% dos clientes são jovens.'.format(jovens))
  print ('{:.0f}% dos clientes são jovens.'.format(adultos)) #prints iguais
  print ('{:.0f}% dos clientes são jovens.'.format(idoso))
#-----------------------------------------------  
def clientes_jovens (cliente_nascimento):
  idade = 0
  cont = 0
  ano_atual = now.year
  quantidade = len(cliente_nascimento)
  porcentagem = 0
  for i in range (len(cliente_nascimento)):
    idade = ano_atual - cliente_nascimento[i]
    if idade >=18 and idade <= 23:
      cont = cont + 1
  if cont != 0:
    porcentagem = (cont / quantidade) * 100  
  return porcentagem
#-----------------------------------------------
def clientes_adulto(cliente_nascimento):
  idade = 0
  cont = 0
  ano_atual = now.year
  quantidade = len(cliente_nascimento)
  porcentagem = 0
  for i in range (len(cliente_nascimento)):
    idade = ano_atual - cliente_nascimento[i]
    if idade >=24 and idade <= 69:
      cont = cont + 1
  if cont != 0:
    porcentagem = (cont / quantidade) * 100  
  return porcentagem
#-----------------------------------------------  
def clientes_idoso(cliente_nascimento):
  idade = 0
  cont = 0
  ano_atual = now.year
  quantidade = len(cliente_nascimento)
  porcentagem = 0
  for i in range (len(cliente_nascimento)):
    idade = ano_atual - cliente_nascimento[i]
    if idade >= 70:
      cont = cont + 1
  if cont != 0:
    porcentagem = (cont / quantidade) * 100 
  return porcentagem
#-----------------------------------------------
def remover_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  codigo_veic_remover = input("Informe codigo do veiculo a ser removido: ")
  indice = busca_verificar(veiculos_codigo, codigo_veic_remover)
  if indice != -1:
    remover_item(veiculos_codigo, indice)
    remover_item(veiculos_modelo, indice)
    remover_item(veiculos_ano, indice)
    print("Veiculo removido com sucesso!")
  else:
    print("\nVeiculo codigo " + codigo_veic_remover + " nao encontrado!")
#-----------------------------------------------
def remover_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento):
  cpf_cli_remover = input("Informe CPF do cliente a ser removido: ")
  indice = busca_verificar(cliente_cpf, cpf_cli_remover)
  if indice != -1:
    remover_item(cliente_codigo, indice)
    remover_item(cliente_cpf, indice)
    remover_item(cliente_nome,indice)
    remover_item(cliente_nascimento, indice)
    print("Cliente removido com sucesso!")
  else:
    print("\nCPF " + cpf_cli_remover + " nao encontrado!")
#-----------------------------------------------
def pesquisar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  codigo_veic_pesquisar = input("Informe o codigo a ser pesquisado: ")
  indice = busca_verificar(veiculos_codigo, codigo_veic_pesquisar)
  if indice != -1:
    v_codigo = veiculos_codigo[indice]
    v_modelo = veiculos_modelo[indice]
    v_ano = veiculos_ano[indice]
    print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))
  else:
    print("\nVeiculo codigo " + codigo_veic_pesquisar + " nao encontrado!")
#-----------------------------------------------
def pesquisar_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento):
  cpf_pesquisar = input("Informe o CPF a ser pesquisado: ")
  indice = busca_verificar(cliente_cpf, cpf_pesquisar)
  if indice != -1:
    cli_codigo = cliente_codigo[indice]
    cli_cpf = cliente_cpf[indice]
    cli_nome = cliente_nome[indice]
    cli_nascimento = cliente_nascimento[indice]
    print("\nCliente codigo: " + cli_codigo + ", CPF: " + cli_cpf + ", Nome: " + cli_nome + ", Nascimento: " + str(cli_nascimento))
  else:
    print("CPF:  " + cpf_pesquisar + " nao encontrado!")
#-----------------------------------------------
def listar_veiculos(veiculos_codigo, veiculos_modelo, veiculos_ano):
  for i in range(len(veiculos_codigo)):
    v_codigo = veiculos_codigo[i]
    v_modelo = veiculos_modelo[i]
    v_ano = veiculos_ano[i]
    print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))
#-----------------------------------------------
def listar_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento):
  for i in range(len(cliente_codigo)):
    cli_codigo = cliente_codigo[i]
    cli_cpf =  cliente_cpf[i]
    cli_nome = cliente_nome[i]
    cli_nascimento = cliente_nascimento[i]
    print("\nCliente codigo: " + cli_codigo + ", CPF: " + cli_cpf + ", Nome: " + cli_nome + ", Nascimento: " + str(cli_nascimento))
#-----------------------------------------------
def cadastar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  v_codigo = input("Informe o codigo: ")
  if busca_verificar(veiculos_codigo, v_codigo) == -1:
    v_modelo = input("Informe o modelo: ")
    v_ano = int(input("Informe o ano de fabricacao: "))
    veiculos_codigo.append(v_codigo)
    veiculos_modelo.append(v_modelo)
    veiculos_ano.append(v_ano)
    print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano) + " cadastrado com sucesso!")
  else:
      print("Codigo " + v_codigo + " ja esta cadastrado!")
#------------------------------------------------
def cadastar_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento):
  cli_codigo = input("Informe o codigo: ")
  if busca_verificar(cliente_codigo, cli_codigo) == -1: # cadastro tem que ser cpf duplicando cpf
    cli_cpf = input("Informe o CPF: ")
    cli_nome = input("Informe o nome:")
    cli_nascimento = int(input("Informe o ano de nascimento: "))
    cliente_codigo.append(cli_codigo)
    cliente_cpf.append(cli_cpf)
    cliente_nome.append(cli_nome)
    cliente_nascimento.append(cli_nascimento)
    print("\nCliente codigo: " + cli_codigo + ", CPF: " + cli_cpf + ", Nome: " +cli_nome + ", Nascimento:"+ str(cli_nascimento)+" cadastrado com sucesso")
  else:
    print("Codigo " + cli_codigo + " ja esta cadastrado!")
#-------------------------------------------------
def gerenciador_submenu_cli_relatorio(clientes_nascimento):
  opcao_submenu_cliente = 'x'
  while opcao_submenu_cliente != '0':
    opcao_submenu_cliente = submenu_cli_relatorio()
    if opcao_submenu_cliente == '1':
      relatorio_idade(clientes_nascimento)
    elif opcao_submenu_cliente == '0':
      print("Obrigado por usar nosso programa!!!") #não esta encerrando? 
    else:
      print("Opcao invalida!!! Escolha novamente!")
#-------------------------------------------------
def gerenciador_submenu_veic_relatorio(veiculos_codigo, veiculos_modelo , veiculos_ano):
  opcao_submenu_veiculo = 'x'
  while opcao_submenu_veiculo != '0':
    opcao_submenu_veiculo = submenu_veic_relatorio()
    if opcao_submenu_veiculo == '1':
      relatorio_modelo(veiculos_modelo)
    elif opcao_submenu_veiculo == '2':
      relatorio_modelo_quantidade(veiculos_modelo)
    elif opcao_submenu_veiculo == '3':
      relatorio_veic_velho(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_submenu_veiculo == '4':
      relatorio_veic_novo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_submenu_veiculo == '5':
      relatorio_ipva(veiculos_ano)    
    elif opcao_submenu_veiculo == '0':
      print("Obrigado por usar nosso programa!!!") #não esta encerrando? 
    else:
      print("Opcao invalida!!! Escolha novamente!") 
#-----------------------------------------------
def gerenciador_relatorio(clientes_nascimento,veiculo_codigo,veiculo_modelo, veiculo_ano):
  opcao_relatorio = 'x'
  while opcao_relatorio != '0':
    opcao_relatorio = menu_relatorios()
    if opcao_relatorio == '1':
      gerenciador_submenu_veic_relatorio(veiculo_codigo,veiculo_modelo, veiculo_ano)
    elif opcao_relatorio == '2':
      gerenciador_submenu_cli_relatorio(clientes_nascimento) 
    elif opcao_relatorio == '0':
      print("Obrigado por usar nosso programa!!!") #não esta encerrando? 
    else:
      print("Opcao invalida!!! Escolha novamente!") 
#-----------------------------------------------
def gerenciador_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  opcao_veiculo ='x'
  while opcao_veiculo != '0':
    opcao_veiculo = menu_veiculo()
    if opcao_veiculo == '1':
      cadastar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '2':
      listar_veiculos(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '3':
      pesquisar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '4':
      remover_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '0':
      print("Obrigado por usar nosso programa!!!") #não esta encerrando? 
    else:
      print("Opcao invalida!!! Escolha novamente!")  
#-----------------------------------------------
def gerenciador_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento):
  opcao_cliente ='x'
  while opcao_cliente != '0':
    opcao_cliente = menu_cliente()
    if opcao_cliente =='1':
      cadastar_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento)
    elif opcao_cliente == '2':
      listar_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento)
    elif opcao_cliente == '3':
      pesquisar_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    elif opcao_cliente == '4':
      remover_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    elif opcao_cliente == '0':
      print( ) #correto!
    else:
      print("Opcao invalida!!! Escolha novamente!") 
#-----------------------------------------------
def submenu_veic_relatorio():
  print("\n**********************************")
  print("Gerenciar Relatorios Veiculo")
  print("   Listar por Modelo................1")
  print("   Listar por Modelo e Quantidade...2")
  print("   Listar por Veiculo mais velho....3")
  print("   Listar por Veiculo mais novo.....4")
  print("   Listar por IPVA..................5")
  print("Sair do Programa....................0") #não seria voltar?
  op = input("-> ")
  return op
#-----------------------------------------------
def submenu_cli_relatorio():
  print("\n**********************************")
  print("Gerenciar Relatorios Clientes")
  print("   Listar por Idade...........1")
  print("Sair do Programa..............0") #não seria voltar?
  op = input("-> ")
  return op
#-----------------------------------------------
def menu_relatorios():
  print("\n**********************************")
  print("Gerenciar Relatorios")
  print("   Relatorios Veiculos.........1")
  print("   Relatorios Clientes.........2")
  print("Sair do Programa...............0") #não seria voltar?
  op = input("-> ")
  return op
#-----------------------------------------------
def menu_veiculo():
  print("\n**********************************")
  print("Gerenciar Veiculos")
  print("   Cadastrar Veiculo...........1")
  print("   Listar Veiculos.............2")
  print("   Pesquisar Veiculos..........3")
  print("   Remover Veiculo.............4")
  print("Sair do Programa...............0") #não seria voltar?
  op = input("-> ")
  return op
#-----------------------------------------------
def menu_cliente():
  print("\n**********************************")
  print("Gerenciar Cliente")
  print("   Cadastrar Cliente............1")
  print("   Listar Clientes..............2")
  print("   Pesquisar Cliente............3")
  print("   Remover Cliente..............4")
  print("Sair do Programa................0") #não seria voltar?
  op = input("-> ")
  return op
#-----------------------------------------------
def menu_principal():
    
  print("\nBem vindos a AF Locadora!")
  print(now.day,'/',now.month,'/',now.year,'  ',now.hour,':',now.minute,)
  print("\n**********************************")
  print("Escolha uma opcao:")
  print("   Gerenciar Veiculos..........1")
  print("   Gerenciar Clientes..........2")
  print("   Gerenciar Relatorios........3")
  print("   Sair do Programa............0")
  op = input("-> ")
  return op
#-----------------------------------------------
def main():
  veiculos_codigo = []
  veiculos_modelo = []
  veiculos_ano = []
  cliente_codigo = []
  cliente_cpf = []
  cliente_nome = []
  cliente_nascimento = []
  
  opcao = 'x'
  while opcao != '0':
    opcao = menu_principal()
    if opcao == '1':
      gerenciador_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano) 
    elif opcao == '2':
      gerenciador_cliente(cliente_codigo, cliente_cpf, cliente_nome, cliente_nascimento)
    elif opcao == '3':
      gerenciador_relatorio(cliente_nascimento,veiculos_codigo,veiculos_modelo, veiculos_ano)  
    elif opcao == '0':
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!")
#-----------------------------------------------

# Programa principal
main()
