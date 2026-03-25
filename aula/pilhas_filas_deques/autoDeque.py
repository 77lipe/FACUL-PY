from collections import deque

historico = deque()

while True:
    escolha = int(input("Qual serviço quer usar: \n1 -- Nova janela\n2 -- Apagar janela\n0 -- Sair"))

    if escolha == 1:
        status = True
        while status == True:
            janela = str(input("Digite o nome da janela que quer adicionar: "))
            opcao = int(input("Em qual lado deseja adicionar uma nova janela: \n1 -- ->\n2 -- <-\n0 -- Voltar"))
            if opcao == 1:
                historico.append(janela)
                print("Histórico atual:", historico)
            elif opcao == 2:
                historico.appendleft(janela)
                print("Histórico atual:", historico)
            elif opcao == 0:
                status = False
    elif escolha == 2:
        status = True
        while status == True:
            opcao = int(input("Qual janela quer remover: \n1 -- Primeira janela (<=)\n2 -- Última janela (=>)\n0 -- Voltar"))
            if opcao == 1:
                historico.popleft()
                print("Histórico atual:", historico)
            elif opcao == 2:
                historico.pop()
                print("Histórico atual:", historico)
            elif opcao == 0:
                status = False