menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
       valor = float(input("Informe o valor do depósito: "))
       
       if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
           
       else:
           print("Operação falhou! O valor informado é inválido")
    
    elif opcao == "s":
       valor = float(input("Informe o valor de saque: "))
       
       if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente")
       
       if valor > limite:
            print("Operação falhou! O valor de saque excede o limite")
           
       
       if numero_saques >= LIMITE_SAQUES:
           print("Operação falhou! Número de saques excedido.")
           
       elif valor > 0 and valor <= limite:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saques +=1
       
    elif opcao == "e":
        print(" Extrato ".center(29,"="))
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print ("="*29)
       
    elif opcao == "q":
       break
   
    else:
       print("Operação inválida, por favor selecione novamente a operação desejada.")
        