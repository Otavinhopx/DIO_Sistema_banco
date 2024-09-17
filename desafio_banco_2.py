from datetime import datetime
import textwrap

saldo_cliente = 0
limite_cliente = 500
numero_saques_limite = 0
extrato_cliente_operacoes = "Operações Realizadas: \n"
LIMITE_SAQUES = 3
usuarios = {}
numero_da_conta = 0
NUMERO_AGENCIA = "0001"

def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar usuário
    [5] Criar conta
    [6] Sair
    
    => """
    return input(textwrap.dedent(menu))

#=====================FUNÇÕES=======================

def saque(*, saldo_cliente, valor, limite_cliente, numero_saques_limite):
    global extrato_cliente_operacoes
    
    if valor > limite_cliente:
        print("Saque maior que o valor limite")
        return saldo_cliente, numero_saques_limite
    
    if valor > saldo_cliente:
        print("Saldo menor que o valor de saque")
        return saldo_cliente, numero_saques_limite
    
    if numero_saques_limite >= LIMITE_SAQUES:
        print("Limite de saques ultrapassados")
        return saldo_cliente, numero_saques_limite
    
    saldo_cliente -= valor
    extrato_cliente_operacoes += f"Saque: R${valor:.2f} {datetime.now()}\n"
    numero_saques_limite += 1
    print("Saque realizado com sucesso")
    return saldo_cliente, numero_saques_limite

def deposito(saldo_cliente, valor, /):
    global extrato_cliente_operacoes
    
    saldo_cliente += valor
    extrato_cliente_operacoes += f"Deposito: R${valor:.2f} {datetime.now()}\n"
    print("Depósito realizado com sucesso")
    print(f"{datetime.now()}")
    return saldo_cliente

def extrato(saldo_cliente, /):
    global extrato_cliente_operacoes
    
    print("Extrato")
    print(f"Seu saldo é de R${saldo_cliente}")
    print(extrato_cliente_operacoes)
    print(f"{datetime.now()}")

def cadastrar_cliente():
    global usuarios
    
    cpf = input("Informe seu cpf(apenas números): ")
    if cpf in usuarios:
        print("CPF já existente")
        return
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    logradouro = input("Informe seu logradouro: ")
    nro = input("Informe o número da sua casa: ")
    bairro = input("Informe seu bairro: ")
    cidade = input("Informe sua cidade: ")
    estado = input("Informe seu estado(sigla): ")
    endereco = f"{logradouro}, {nro}, {bairro}, {cidade}, {estado}"
    
    usuarios[cpf] = {
        "nome" : nome,
        "data_nascimento" : data_nascimento,
        "CPF" : cpf,
        "endereco" : endereco,
        "contas": []
    }
    
    print("Conta criada!")
     
def criar_conta(NUMERO_AGENCIA):
    global usuarios
    global numero_da_conta
    
    if not usuarios:
        return print("Nenhum usuário cadastrado!")
    
    cpf = input("Insira seu CPF: ")
    
    if cpf not in usuarios:
        print("Usuário não encontrado no banco de dados.")
        return
    
    conta = {
        "conta_cliente" : f"{numero_da_conta}{NUMERO_AGENCIA}"
    }
    
    usuarios[cpf]['contas'].append(conta)
    numero_da_conta += 1
    print("Conta criada com sucesso!")

while True:
    opcao = menu()

    if opcao == "1":
        print("Depósito")
        valor = float(input("Insira o valor desejado R$"))
        saldo_cliente = deposito(saldo_cliente, valor)

    elif opcao == "2":
        print("Saque")
        valor = float(input("Insira o valor desejado para saque com o limite de R$500,00: R$"))
        saldo_cliente, numero_saques_limite = saque(saldo_cliente=saldo_cliente, valor=valor, limite_cliente=limite_cliente, numero_saques_limite=numero_saques_limite)

    elif opcao == "3":
        extrato(saldo_cliente)

    elif opcao == "4":
        cadastrar_cliente()

    elif opcao == "5":
        criar_conta(NUMERO_AGENCIA)
        
    elif opcao == "6":
        break
    
    else:
        print("Operação inválida")