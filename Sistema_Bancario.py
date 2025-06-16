menu = """

[D] Deposito
[S] Saque
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite =  500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3


nome = input("Digite seu nome :")
print()
print(f"Seja bem- vindo " + nome.title()) 
print()
print("=> Escolha a sua opção abaixo ! <=")

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito : R${valor:.2f}\n"
            print()
            print(f"Deposito no valor de R${valor:.2f} efetuado com sucesso ")
        
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_valor = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_valor:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! Você não tem limites para saque")

        elif excedeu_saques:
            print("Operação falhou! Limite de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques +=1
            print()
            print(f"Saque no valor de R$ {valor:.2f} efetuado com sucesso!")

        else:
            print("Operacao falhou! O valor informado é invalido.")
 
    elif opcao == "E":
        print("\n========== EXTRATO - RoBanK ==========")
        print("Não foram realizados movimentações: " if not extrato else extrato)
        print(f"\nS a l d o: R${saldo:.2f}")
        print("=======================================")
    
    elif opcao == "Q":
        break

else:
    print("Operação inválida, por favor seleciona novamente a operação desejada.")
    