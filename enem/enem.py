import databasesqlite as banco

# o .db é a extensão do sqlite!
#é o brigatório passa a extensão no final do  arquivo!


# -- INT MYSLQ , INTEGER SQLITE
# -- AUTO_INCREMENT MYSQL , AUTOINCREMENT SQLITE
# -- DECIMAL(10,2) MYSQL, REAL (10,2)
banco.config(r"E:\Alice Silva\backend\atividades\enem\bancoenem.db")

def criar_tabelas():
    banco.execute_non_query("""
    CREATE TABLE IF NOT EXISTS questoes(
        id INTEGER primary key autoincrement ,
        materia varchar(255),
        ano date,
        enunciado varchar(255),
        opcao_A char(1),
        opcao_B char(1),
        opcao_C char(1),
        opcao_D char(1),
        opcao_E char(1),
        resposta_correta char(1)              
    );
    """)

    banco.execute_non_query("""
    CREATE TABLE IF NOT EXISTS resultados (
        id INTEGER primary key autoincrement,
        nome_aluno varchar(255),
        resposta char(1),
        QUESTOES_FEITAS INTEGRER,
        QUESTOES_ACERTADAS INTEGRER,
        QUESTOES_ERRADAS INTEGRER,
        acertou boolean,
        FOREIGN KEY (id) REFERENCES questoes(id) 
    );
    """)

    banco.execute_non_query("""
    CREATE TABLE IF NOT EXISTS professores(
    CPF INTEGER primary key,
    nome_prof varchar(255),
    materia varchar(255)                        
    );
    """)


    print("Tabelas criadas com sucesso!")


def menu():
    print("")
    
    print("""
    ================ SIMULADOS DO ENEM ==================

    =====================================================
    1-Cadastrar Professor    

    2-Cadastrar Questão (Apenas Professor)

    3-Listar Questões Cadastradas

    4-Excluir Questão (Apenas Professor)

    5-Fazer Simulado (Aluno responde todas as questões)

    6-Ver Histórico de Desempenho

    7-Sair
    =====================================================""") 

def cadastrar_professor():
    print("Você escolheu, CADASTRAR PROFESSOR!")
    print("")
    cpf = int(input("Digite seu CPF: "))
    professor = input("Digite seu nome: ")
    ensino = input("Digite a matéria com a qual você trabalha: ")

    sql=""
    sql=f"""
    INSERT INTO professores(CPF,nome_prof,materia) VALUES(
    {cpf},'{professor}','{ensino}')
    """
    banco.execute_non_query(sql)
    print("Professor cadastrado com sucesso!")
    print("")

def cadastrar_questao():
    print("Você escolheu,CADASTRAR QUESTÃO!")
    print("")
    digite_cpf=int(input("Digite seu CPF:  "))
    sql=""
    sql=f"""SELECT *FROM professores WHERE CPF={digite_cpf} """
    var1 = banco.execute_query(sql)

    if var1:
        print("Acesso liberado!!")
        print("")
        materia=input("Digite a matéria correspondente à questão: ")
        ano=input("Digite o ano da questão (YYYY-MM-DD): ")
        enun=input("Digite o enunciado da questão: ")
        op_a=input("Digite a alternativa A: ")
        op_b=input("Digite a alternativa B: ")
        op_c=input("Digite a alternativa C: ")
        op_d=input("Digite a alternativa D: ")
        op_e=input("Digite a alternativa E: ")
        correta=input("Digite a letra da alternativa correta: ").upper()

        sql=""
        sql=f"""
        INSERT INTO questoes (materia,ano,enunciado,opcao_A,opcao_B,opcao_C,opcao_D,opcao_E,resposta_correta)
        VALUES('{materia}','{ano}','{enun}','{op_a}','{op_b}','{op_c}','{op_d}','{op_e}','{correta}')
        """
        banco.execute_non_query(sql)
        print("Questão Cadastrada...")
    else:
        print("Seu CPF não está cadastrado em PROFESSORES! Não é possível cadastrar questão.")


def listar_questao():
    sql=""
    sql=""" SELECT * FROM questoes; """
    dados = banco.execute_query(sql)
    print("Você escolheu,LISTAR QUESTÃO!")
    if dados:
        for questao in dados:
            
            print(f"""
            QUESTÃO: {questao["id"]}
            ENUNCIADO: {questao["enunciado"]}
            ALTERNATIVAS: A){questao["opcao_A"]} B){questao["opcao_B"]} C){questao["opcao_C"]} D){questao["opcao_D"]} E){questao["opcao_E"]}
            ALTERNATIVA CORRETA: {questao["resposta_correta"]}       
            """)
    else:
        print("NENHUMA QUESTÃO CADASTRADA!")

def excluir_questao():
    print("Você escolheu,EXCLUIR QUESTÃO!")
    print("")
    digite_cpf=int(input("Digite seu CPF:  "))
    sql=""
    sql=f"""SELECT *FROM professores WHERE CPF={digite_cpf} """
    var1 = banco.execute_query(sql)

    if var1:
        listar_questao()
        id = int(input("Digite o numero da questão que deseja apagar:"))
        sql =""
        sql=f"""DELETE FROM questoes WHERE ID = {id}"""

        banco.execute_non_query(sql)
        print("Questão deletada com sucesso!")
    else:
        print("Não foi possível deletar a questão...")

def simulado():
    quest = 0 
    pontuacao = 0 
    nome_aluno = input("Digite o nome do aluno: ")
    
    sql=""
    sql=F""" INSERT INTO resultados(nome_aluno) VALUES (
    '{nome_aluno}')"""
    banco.execute_non_query(sql)

    print("INICIANDO O SIMULADO")
    sql=""
    sql=" SELECT *FROM questoes;"

    questoes = banco.execute_query(sql)

    if not questoes:
        print("Não há nenhuma questão cadastrada...")
    else:
        for qs in questoes:
            print(f"""
            ================ QUESTÃO {qs["id"]} ==================
            Matéria : {qs["ano"]}
            
            {qs["enunciado"]}
            A){qs["opcao_A"]} B){qs["opcao_B"]} C){qs["opcao_C"]} D){qs["opcao_D"]} E){qs["opcao_E"]}
            """)

            resposta = input("Qual a resposta correta?: ").upper()

            if resposta == qs['resposta_correta']:
                print("Resposta certa!")
                quest = quest+1
                pontuacao = pontuacao+1
            else:
                print(f"Resposta incorreta! Resposta correta: {qs['resposta_correta']}")
                quest= quest+1

        print("")
        print("================ RESULTADO DO SIMULADO ==================")
        print("Questões feitas: ", quest)
        print(f"Pontuação total: {pontuacao}")
        erros = quest - pontuacao
        print("Quantidade de erros:", erros)

        sql=""
        sql=f""" INSERT INTO resultados (nome_aluno,resposta_correta,QUESTOES_ACERTADAS,QUESTOES_ERRADAS)
        VALUES ('{nome_aluno}','{quest}',{erros},{pontuacao})
        """

        banco.execute_non_query(sql)


def historico():
    sql=""
    sql=""" 
    SELECT * FROM resultados    
    """
    dados = banco.execute_query(sql)
    print("=== RESULTADO DE SIMULADOS ANTERIORES: ===")
    if dados:
        for resul in dados:
            print(f"""
            Total: {resul["resposta_correta"]}
            NOME ALUNO: {resul["nome_aluno"]}
            QUESTOES_ERRADA: {resul["QUESTOES_ERRADAS"]}
            QUESTOES_CERTAS: {resul["QUESTOES_ACERTADAS"]}
        """)
    else:
        print("NENHUM SIMULADO FEITO!")



