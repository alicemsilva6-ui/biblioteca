import enem as app


app.criar_tabelas()

app.menu()

opcao = 0 

while opcao !=7:
    app.menu()
    opcao = int(input("Digite um opção: "))
    print("")
    
    if opcao ==1:
        app.cadastrar_professor()
    elif opcao ==2:
        app.cadastrar_questao() 
    elif opcao == 3:
        app.listar_questao()
    elif opcao ==4:
        app.excluir_questao()
    elif opcao == 5:
        app.simulado()
    elif opcao ==6:
        app.historico()
    elif opcao==7:
        print("programa encerrado!")
        break