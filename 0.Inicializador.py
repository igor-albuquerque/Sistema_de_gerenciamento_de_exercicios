from Cadastro import Cadastro
from Login import login
from Exercicio import Exercicio
from BuscaExercicios import por_materia, por_tipo, todos_exercicios, sortear, conferirAtualizacao, stringExercicio, conferirAtualizacao2
from Connection import Connection
from Feedback import desempenhoAluno, desempenhoMedioSala
import os

def clear():
    os.system('cls')

def cadastro():
    nome = input('Nome: ')
    login = input('Login: ')
    senha = input('Senha: ')
    tipo = input('Você é professor ou aluno? ')
    try: 
        usuario = Cadastro(nome, login, senha, tipo)
        usuario.cadastrar()
    except ValueError:
        print('Não foi possível realizar o cadastro.')
        print('Tente novamente!')

def entrar():
    x = False
    while x==False:
        opcao = input('Tem conta(1) ou deseja cadastrar uma(2)?')
        print('-----------------------------------------')
        if opcao == '1':
            print('Insira seu login e senha de usuário')
            usuario = input('login: ')
            senha = input('senha: ')
            entrou = login(usuario,senha)
            if entrou[0]==True:
                x==True
                clear()
                print('Login efetuado com sucesso!')
                if entrou[1]=='professor':
                    return ['professor']
                else:
                    return ['aluno',entrou[2]]
            else:
                clear()
                print('Usuário ou senha inválidos')
        elif opcao=='2':
            cadastro()
        else:
            print('Opção inválida! Tente novamente!')

def cadastrarExercicio():
    tipo = input('Qual é o tipo de exercício? Dissertativo(1), múltipla-escolha(2) ou verdadeiro/falso(3)')
    materia = input('Qual é a matéria? ES, POO, BD, AC, CA ')
    pergunta = input('Digite o exercício/pergunta: ')
    if tipo=='2':
        opcao1 = input('a)')
        opcao2 = input('b)')
        opcao3 = input('c)')
        opcao4 = input('d)')
        pergunta = f'{pergunta} \n a){opcao1} \n b){opcao2} \n c){opcao3} \n d){opcao4}'        

    resposta = input('Qual seria a resposta? ')
    try: 
        ex = Exercicio(tipo, materia, pergunta,resposta)
        ex.cadastrar_ex()
        clear()
        print('Exercício cadastrado com sucesso!')
    except ValueError:
        print('Erro!!!')

def listarExercicios():
    clear()
    print('-----------------------------------------------')
    print('Quais exercícios devem ser listados?')
    print('1 - Todos os exercícios')
    print('2 - Listar por tipo de questão')
    print('3 - Listar por matéria')
    print('4 - Sortear um exercício aleatório\n')
    x = input()
    if x=='1':
        ex = todos_exercicios()
        stringExercicio(ex, 0, False)

    elif x=='2':
        p = True
        tipo = input('Qual é o tipo de exercício? Dissertativo(1), múltipla-escolha(2) ou verdadeiro/falso(3)')
        if tipo=='1':
            ex = por_tipo('Dissertativa')
        elif tipo=='2':
            ex = por_tipo('Multipla Escolha')
        elif tipo=='3':
            ex = por_tipo('Verdadeiro/Falso')
        else: 
            print("Opção inválida!!!\n")
            p = False
        
        if p==True:
            stringExercicio(ex, 0, False)  

    elif x=='3':
        m = input('Qual matéria? POO,ES,BD,AC ou CA ')
        if m=='POO' or m=='ES' or m=='BD' or m=='AC' or m=='CA':
            ex = por_materia(m)
            stringExercicio(ex, 0, False)
        else:
            print('Opção Inválida!!')

    elif x=='4':
        ex = sortear()
        print('---------------------------------------------')
        print('Exercício Sorteado!\n')
        print(f"Tipo: {ex['tipo']}")
        print(f"{ex['materia']}")
        print(f"{ex['exercicio']}")
        input('\n Pressione enter para continuar!') 

    else:
        print('Opção inválida!!')
        clear()
    clear()

def atualizarExercicios():
    clear()
    print('Qual exercício precisa ser atualizado?')
    exercicio = input('Digite o exercício que será modificado: ')
    filtro = {'exercicio': exercicio}
    opcao = input('Deseja mudar o tipo(1), a matéria(2), o exercício(3) ou a resposta(4)?')
    if opcao=='1':
        try:
            connect = Connection('Exercicios')
            novoTipo = input('Qual será o tipo do exercício? Dissertativa(1), múltipla escolha(2) ou verdadeiro/falso(3) ')
            atualiza = conferirAtualizacao(opcao,novoTipo)
            alteracoes = {'$set': {'tipo': atualiza}}
            resultado = connect.colecao.update_one(filtro, alteracoes)
            connect.fechar_conexao()
            clear()
            print('Atualização feita com sucesso!!')
        except ValueError:
            clear()
            print('Valor inválido!!')
            print('Não foi possível fazer a atualização')

    elif opcao=='2':
        try: 
            connect = Connection('Exercicios')
            novaMateria = input('Qual será a nova matéria? ')
            novaMateria = conferirAtualizacao(opcao, novaMateria)
            alteracoes = {'$set': {'materia': novaMateria}}
            resultado = connect.colecao.update_one(filtro, alteracoes)
            connect.fechar_conexao()
            clear()
            print('Atualização feita com sucesso!!')
        except ValueError:
            clear()
            print('Valor inválido!!')
            print('Não foi possível fazer a atualização')

    elif opcao=='3':
        connect = Connection('Exercicios')
        novoExercicio = input('Digite o exercício: ')
        alteracoes = {'$set': {'exercicio': novoExercicio}}
        resultado = connect.colecao.update_one(filtro, alteracoes)
        connect.fechar_conexao()
        clear()
        print('Atualização feita com sucesso!!')
    elif opcao=='4':
        try:
            connect = Connection('Exercicios')
            tipo = input('Qual é o tipo do exercício? Dissertativa(1), múltipla escolha(2) ou verdadeiro/falso(3)')
            novaResposta = input('Qual será a resposta para esse exercício? ')
            novaResposta = conferirAtualizacao2(opcao,novaResposta,tipo)
            alteracoes = {'$set': {'resposta': novaResposta}}
            resultado = connect.colecao.update_one(filtro, alteracoes)
            connect.fechar_conexao()
            clear()
            print('Atualização feita com sucesso!!')
        except ValueError:
            clear()
            print('Valor inválido!!')
    else:
        clear()
        print('Opção inválida!')

def resolverExercicios(nome):
    clear()
    print('-----------------------------------------------')
    print('Quais exercícios você quer resolver?')
    print('1 - Todos os exercícios')
    print('2 - Listar por tipo de questão')
    print('3 - Listar por matéria')
    x = input()
    if x=='1':
        ex = todos_exercicios()
        resposta = stringExercicio(ex,1,nome)
    elif x=='2':
        clear()
        p = True
        tipo = input('Qual é o tipo de exercício? Dissertativo(1), múltipla-escolha(2) ou verdadeiro/falso(3)')
        if tipo=='1':
            ex = por_tipo('Dissertativa')
            resp = 2
        elif tipo=='2':
            ex = por_tipo('Multipla Escolha')
            resp=1
        elif tipo=='3':
            ex = por_tipo('Verdadeiro/Falso')
            resp=1
        else: 
            print("Opção inválida!!!\n")
            p = False
        if p==True:
            stringExercicio(ex,resp,nome)  

    elif x=='3':
        clear()
        m = input('Qual matéria? POO,ES,BD,AC ou CA ')
        if m=='POO' or m=='ES' or m=='BD' or m=='AC' or m=='CA':
            ex = por_materia(m)
            stringExercicio(ex,1,nome)
        else:
            print('Opção Inválida!!')

    else:
        print('Opção inválida!')

def receberFeedback(tipo, nome):
    if tipo=='professor':
        print('Você quer ver o desempenho de algum aluno(1) ou o desempenho médio da sala inteira(2)?')
        x = input()
        if x=='1':
            clear()
            aluno = input('Qual é o nome do aluno? ')
            desempenhoAluno(aluno)
        elif x=='2':
            clear()
            desempenhoMedioSala()
        else:
            print('Opção inválida!')
    else:
        clear()
        desempenhoAluno(nome)

tipo = entrar()

if tipo[0]=='professor':
    x = True
    while x==True:
        print('--------------------------------------------')
        print('O que deseja fazer?')
        print('1 - Cadastrar novo exercício?')
        print('2 - Receber Feedback dos alunos')
        print('3 - Listar exercícios disponíveis')
        print('4 - Atualizar exercícios')
        print('5 - Sair do sistema')
        resposta = input()
        if resposta=='1':
            clear()
            cadastrarExercicio()
        elif resposta=='2':
            clear()
            receberFeedback(tipo[0],False)
            pass
        elif resposta=='3':
            clear()
            listarExercicios()
        elif resposta=='4':
            clear()
            atualizarExercicios()
        elif resposta == '5':
            clear()
            print('Log out realizado')
            x = False
        else:
            print('Opção Inválida! Tente novamente')
else:
    x = True
    while x==True:
        print('--------------------------------------------')
        print('O que deseja fazer?')
        print('1 - Resolver alguns exercícios')
        print('2 - Receber Feedback')
        print('3 - Listar exercícios')
        print('4 - Sair do sistema')
        resposta = input()
        if resposta=='1':
            clear()
            resolverExercicios(tipo[1])
        elif resposta=='2':
            clear()
            receberFeedback(tipo[0],tipo[1])
        elif resposta=='3':
            clear()
            listarExercicios()
        elif resposta == '4':
            clear()
            print('Log out realizado')
            x = False
        else:
            print('Opção Inválida! Tente novamente')