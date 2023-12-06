from Connection import Connection

class Exercicio:
  def __init__(self, tipo, materia,exercicio,resposta):
    self.tipo = tipo #Dissertativo, múltipla-escolha ou verdadeiro/falso
    self.materia = materia 
    self.exercicio = exercicio
    self.resposta = resposta

  @property
  def tipo(self):
    return self.__tipo

  @property
  def materia(self):
    return self.__materia

  @property
  def exercicio(self):
    return self.__exercicio

  @property
  def resposta(self):
    return self.__resposta
  
  @materia.setter
  def materia(self,materia):
    if len(materia)>0:
      if materia=='ES' or materia=='POO' or materia=='AC' or materia=='CA' or materia=='BD':
        self.__materia = materia
      else:
        print('Matéria inválida')
        raise ValueError
    else:
      raise ValueError
  
  @tipo.setter
  def tipo(self,tipo):
    if len(tipo)>0 or len(tipo)<2:
      if tipo=='1':
        tipo = 'Dissertativa'
        self.__tipo = tipo
      elif tipo=='2':
        tipo='Multipla Escolha'
        self.__tipo = tipo
      elif tipo=='3':
        tipo='Verdadeiro/Falso'
        self.__tipo = tipo
      else:
        raise ValueError
    else:
      raise ValueError

  @exercicio.setter
  def exercicio(self,exercicio):
    if len(exercicio)>15:
      self.__exercicio = exercicio
    else:
      raise ValueError

  @resposta.setter
  def resposta(self,resposta):
    if self.tipo=='Dissertativa' and len(resposta)>3: 
      self.__resposta = resposta
    elif self.tipo=='Multipla Escolha' and len(resposta)<=2:
      self.__resposta = resposta
    elif self.tipo=='Verdadeiro/Falso' and len(resposta)>0:
      if resposta=='Verdadeiro' or resposta=='Falso':
        self.__resposta = resposta
      else:
        print('Resposta inválida')
        raise ValueError
    else:
      raise ValueError

  def cadastrar_ex(self):
    connect = Connection('Exercicios')

    json = {
      "tipo":f"{self.tipo}",
      "materia":f"{self.materia}",
      "exercicio":f"{self.exercicio}",
      "resposta":f"{self.resposta}"
    }
    insercao = connect.colecao.insert_one(json)
    connect.fechar_conexao()


 