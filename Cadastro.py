from Connection import Connection

class Cadastro:
  def __init__(self, nome, login, senha, tipo):
    self.nome = nome
    self.login = login
    self.senha = senha
    self.tipo = tipo  #professor ou aluno

  @property
  def nome(self):
    return self.__nome

  @property
  def login(self):
    return self.__login

  @property
  def senha(self):
    return self.__senha

  @property
  def tipo(self):
    return self.__tipo

  @nome.setter
  def nome(self, nome):
    if len(nome) > 0:
      self.__nome = nome
    else:
      raise ValueError

  @login.setter
  def login(self, login):
    if len(login) > 4:
      # if not self.verificacao():
      self.__login = login
    else:
      raise ValueError('Login deveria ser maior')

  @senha.setter
  def senha(self, senha):
    self.__senha = senha

  @tipo.setter
  def tipo(self, tipo):
    if tipo == 'professor' or tipo == 'aluno':
      self.__tipo = tipo
    else:
      raise ValueError("Deve ser 'professor' ou 'aluno'")
    
  def cadastrar(self):
    connect = Connection('Cadastro')

    json = {
      "nome":f"{self.nome}",
      "login":f"{self.login}",
      "senha":f"{self.senha}",
      "tipo":f"{self.tipo}"
    }

    insercao = connect.colecao.insert_one(json)
    connect.fechar_conexao()

  def verificacao(self,login):
    connect = Connection('Cadastro')
    filtro = connect.colecao.find_one({"login":login})    
    connect.fechar_conexao()
    return filtro is not None

