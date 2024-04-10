menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
lim_saque = 500
LIMITE_DIA = 3
extrato =''
numero_de_saques = 0

while True:
  opcao = input(menu)
  if opcao == 'd':
    deposito = float(input('Qual valor deseja depositar? '))
    if deposito > 0:
      saldo += deposito
      extrato += f"Deposito de R${deposito:.2f}\n"
    else:
      print("==========================================")
      print("O Valor a ser depositado deve ser maior que zero")

  elif opcao == 's':
    if numero_de_saques < LIMITE_DIA:
      saque = float(input("Quanto voçê deseja sacar? "))
      if saque <= saldo and saque <= 500:
        saldo -= saque
        extrato += f"Saque de R${saque:.2f}\n"
        numero_de_saques +=1
      else:
        print("==========================================")
        print("Saldo insuficiente ou tentativa de saque maior que 500 reais")
    else:
      print("==========================================")
      print("Voçê atingiu o limite de Saques diarios")

  elif opcao == 'e':
    print("\n================ EXTRATO ================")
    if not extrato:
      print('Voçe nao fez movimentações')
    print(f"{extrato}\n")
    print(saldo)
    print("==========================================")

  elif opcao == 'q':
    break