from Connection import Connection

def login(usuario,senha):
    connect = Connection('Cadastro')
    verifica = connect.colecao.find_one({'login':usuario, 'senha':senha})
    connect.fechar_conexao()

    if verifica is not None:
        return [True,verifica['tipo'],verifica['nome']]
    else:
        return  [False]

