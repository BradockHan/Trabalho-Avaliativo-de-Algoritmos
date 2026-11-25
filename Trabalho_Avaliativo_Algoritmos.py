print("=== ESTACIONAMENTO — PÁTIO ===\n1 - Registrar placa de entrada\n2 - Visualizar veículos no pátio\n3 - Ver quantidade de veículos\n4 - Verificar se uma placa está no pátio\n5 - Registrar saída (remover placa)\n0 - Sair")
placas = []
opcao = int(input("Escolha uma opção:\n"))

while opcao != 0:
  match opcao:

    case 1:
      resgistro_placa = input("Informe a placa do veículo: ")
      if resgistro_placa not in placas:
        placas.append(resgistro_placa)
        print(f"Placa {resgistro_placa} registrada com sucesso!")
        
      else:
        print(f"Placa {resgistro_placa} já esta registrada!")
       


    case 2:
      if len(placas) == 0:
        print("Não há veículos registrados no momento!")
        
      else:
        print(f"Veículos registrados: {placas}")
        


    case 3:
      print(f"O estacionamento possui {len(placas)} veículos registrados.")
      


    case 4:
      verificar = input("Informe a placa ")
      if verificar not in placas:
        print(f"Placa {verificar} não encontrada!")
      else:
        print(f"Placa {verificar} encontrada no estacionamento. ")

    case 5:
      if remover_placa in placas:
           placas.remove(remover_placa)
           print(f"Placa {remover_placa} removida com sucesso!")
           
      else:
        print(f"Placas {remover_placa} não encontrada!")
     
    case _:
      print("Opção Inválida!")
  opcao = int(input("=== ESTACIONAMENTO — PÁTIO ===\n1 - Registrar placa de entrada\n2 - Visualizar veículos no pátio\n3 - Ver quantidade de veículos\n4 - Verificar se uma placa está no pátio\n5 - Registrar saída (remover placa)\n0 - Sair\n"))
  print("\n"*3)

print("Saída registrada!\nVolte Sempre! ;) ")