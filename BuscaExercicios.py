from Connection import Connection
import os
import random

def por_tipo(tipo):
    connect = Connection('Exercicios')
    exercicios = list(connect.colecao.find({'tipo': tipo}))
    connect.fechar_conexao()
    return exercicios

def por_materia(materia):
    connect = Connection('Exercicios')
    exercicios = list(connect.colecao.find({'materia':materia}))
    connect.fechar_conexao()
    return exercicios

def todos_exercicios():
    connect = Connection('Exercicios')
    exercicios = list(connect.colecao.find())
    connect.fechar_conexao()
    return exercicios

def sortear():
    tipos = ['Dissertativa','Multipla Escolha','Verdadeiro/Falso'] 
    materias = ['POO','ES','BD','AC','CA']
    tipoSorteio = random.randint(0,2)
    materiaSorteio = random.randint(0,4)
    connect = Connection('Exercicios')
    exercicio = connect.colecao.find_one({"materia":materias[materiaSorteio],"tipo":tipos[tipoSorteio]})
    connect.fechar_conexao()
    if exercicio:
        return exercicio

def conferirAtualizacao2(opcao,valor,tipo):
    if opcao=='4':
        if tipo=='1' and len(valor)>3:
            return valor
        elif tipo=='2' and len(valor)<=2:
            return valor
        elif tipo=='3' and len(valor)>0:
            if valor=='Verdadeiro' or valor=='Falso':
                return valor
            else:
                print('Válor inválido')
                raise ValueError
        else:
            print('Valor inválido')
            raise ValueError

def conferirAtualizacao(opcao, valor):
    if opcao=='1':
        if len(valor)>0 or len(valor)<2:
            if valor=='1':
                valor = 'Dissertativa'
            elif valor=='2':
                valor='Multipla Escolha'
            elif valor=='3':
                valor='Verdadeiro/Falso'
            else:
                raise ValueError
        else:
            raise ValueError
        return valor
    elif opcao=='2':
        if len(valor)>0:
            if valor=='POO' or valor=='ES' or valor=='BD' or valor=='AC' or valor=='CA':
                return valor
            else:
                raise ValueError
        else:
            raise ValueError
    elif opcao=='3':
        if len(valor)>15:
            return valor
        else:
            print('Valor Inválido')
            raise ValueError


def gerarTextoFeedback(acertos,total):
    if acertos == total:
        return f"Ótimo! Acertou todas as {total} questões respondidas."
    else:
        return f"Acertou {acertos} de {total} questões."  

def stringExercicio(ex, responder,nome):
    os.system('cls')

    respostas = []
    acertos = 0
    for i in range(len(ex)):
        print('---------------------------------------------')
        print(f"Exercício {i+1}\n")
        print(f"Tipo: {ex[i]['tipo']}")
        print(f"{ex[i]['materia']}")
        print(f"{ex[i]['exercicio']}")

        if responder==0:
            input('\n Pressione enter para continuar!')
        else:
            r = input('Digite a resposta: ')
            if ex[i]['tipo']=='Dissertativa':
                y = [ex[i]['exercicio'],r]
                connect = Connection('Dissertativas')
                dissertativa = {
                    'nome':nome,
                    'exercicio':y[0],
                    'resposta': y[1]
                }
                connect.colecao.insert_one(dissertativa)
                connect.fechar_conexao()

            else:
                respostas.append(r)
                r = r.lower()
                resposta = ex[i]['resposta']
                if r==resposta:
                    acertos += 1
        total = len(respostas)
    
    if responder==1:
        feedback = {
            'nome': nome,
            'acertos': acertos,
            'percentual': (acertos/total)*100,
            'total': total,
            'texto_feedback': gerarTextoFeedback(acertos, total)
        }
        connect = Connection('Feedback')
        insercao = connect.colecao.insert_one(feedback)
        connect.fechar_conexao()



    

