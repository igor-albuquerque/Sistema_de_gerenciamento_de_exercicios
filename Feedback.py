from Connection import Connection

def desempenhoAluno(nome):
    connect = Connection('Feedback')
    desempenho = connect.colecao.find_one({'nome':nome})
    connect.fechar_conexao()
    connect2 = Connection('Dissertativas')
    respostasDissertativas = list(connect2.colecao.find({'nome':nome}))
    connect2.fechar_conexao()

    if desempenho is not None:
        print('--- Desempenho do Aluno ---')
        print(f'Nome: {nome}')
        print(desempenho.get('texto_feedback', 'Texto de feedback não encontrado.'))
        print(f"Percentual de acerto: {desempenho.get('percentual', 'Percentual não encontrado.')}")
        print('----------------------------\n')
    else:
        print(f'Desempenho não encontrado para o aluno {nome}')

    input('Aperte enter para continuar')

    if respostasDissertativas is not None:
        print('\n--- Respostas das questões dissertativas ---')
        print(f"Nome: {nome}")
        for j in range(len(respostasDissertativas)):
            print(f"\nExercício: {respostasDissertativas[j]['exercicio']}")
            print(f"Resposta: {respostasDissertativas[j]['resposta']}")
            input('\nAperte enter para continuar')
    else:
        print("\nNão foram realizadas questões dissertativas por esse aluno")

def desempenhoMedioSala():
    connect = Connection('Feedback')
    desempenho = list(connect.colecao.find())
    connect.fechar_conexao()
    connect2 = Connection('Dissertativas')
    respostasDissertativas = list(connect2.colecao.find())
    connect2.fechar_conexao()
    somaAcertos = 0
    somaTotal = 0
    
    if desempenho is not None:
        print('--- Desempenho médio dos alunos ---')
        for i in range(len(desempenho)):
            acertos = desempenho[i]['acertos']
            total = desempenho[i]['total']
            somaAcertos += int(acertos)
            somaTotal += int(total)
    
        percentual = (somaAcertos/somaTotal)*100
        print(f'Percentual de acertos da sala: {percentual:.2f}%\n')
        input('\n Aperte enter para continuar')

    if respostasDissertativas is not None:
        print('--- Respostas das perguntas dissertativas ---')
        for i in range(len(respostasDissertativas)):
            print('--------------------------------------------')
            print(f"Nome: {respostasDissertativas[i]['nome']}")
            print(f"Exercício: {respostasDissertativas[i]['exercicio']}\n")
            print(f"Resposta: {respostasDissertativas[i]['resposta']}")

