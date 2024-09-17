saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print ("Depósito")
        deposito = float(input("Insira o valor desejado R$"))
        saldo = saldo + deposito
        print("Depósito realizado com sucesso")
        
    elif opcao == "2":
        print("Saque")
        saque = float(input("Insira o valor desejado para saque com o limite de R$500,00: R$"))
        if saque <= limite:
            if saque < saldo:
                if numero_saques < LIMITE_SAQUES:
                    saldo = saldo - saque
                    numero_saques += 1
                    print("Saque realizado com sucesso")
                else:
                    print("Limite de saques ultrapasssado")
            else:
                print("Saldo menor que o valor de saque")
        else:
            print("Saque maior que o valor limite")
            
    elif opcao == "3":
        print("Extrato")
        print(f"Seu saldo é de R${saldo}")
        
    elif opcao == "4":
        break
    
    else:
        print("Operação inválida")