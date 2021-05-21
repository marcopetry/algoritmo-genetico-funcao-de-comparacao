from utils import getOperators, randomInt
from Person import getAtributesPerson
import random

class Formula:
  def __init__(self, persons):
    self.formula = None
    self.persons = persons
    self.fitnessValue = None
    self.validFormula = True
  
  def createFormula(self):
    operators = getOperators()

    atributes = getAtributesPerson()
    random.shuffle(atributes)
    formula = ''
    count = 0
    corte_crossover = randomInt(2, 4)
    try:
      while len(atributes) > 0 and count < 3: #Pega todos os atributos e se gerar forma inválida ele tenta mais 2 vezes gerar um fórmula matemática válida
        sortNumber = random.randrange(0, len(atributes))
        atribute = atributes[sortNumber]
        atributes.remove(atribute)

        sortNumber = random.randrange(0, len(operators))
        sortNumber_two = random.randrange(0, len(operators))
        if(len(atributes) > 0):
          formula = formula + '(' + atribute + operators[sortNumber] + str(randomInt(0, 5)) + ')' + operators[sortNumber_two]
        else:
          formula = formula + atribute
        
        
        if len(atributes) == corte_crossover:
          formula = formula + '|' # usado para fazer o corte na fórmula na hora de cruzar
        self.formula = formula

      self.calcPriorityPerson()
    except:
      count += 1
      self.createFormula()
    self.formula = formula

  def setFormula(self, formula):
    self.formula = formula
  
  def printFormula(self):
    print(self.formula)
  
  def calcPriorityPerson(self):
    atributes = getAtributesPerson()
   
    for person in self.persons:
      formulaComNumeros = self.formula.replace('|', '')
      for attr in atributes:
        formulaComNumeros = formulaComNumeros.replace(attr, str(getattr(person, attr)))
      try:
        calcValue = eval(formulaComNumeros)
        if calcValue < 0:
          calcValue *= -1

        person.setPriority(calcValue)
        self.validFormula = True
      except:
        person.setPriority(0)
        self.fitnessValue = 99999999999
        self.validFormula = False
          
  def sortPersons(self):
    self.persons.sort(reverse=True, key=lambda ind : ind.priority)

  def fitness(self, list_corretct_priority):
    if self.validFormula: 
      # se a fórmula é válida e não gera erros na hora do cálculo
      # aqui é calculado a distância do item para onde ele devia estar
      # quanto menor esse valor quer dizer que os itens estavam ou no lugar ou próximos dele
      # 0 seria o resultado ótimo
      try:
        self.calcPriorityPerson()
        self.sortPersons()
        #lista com os ids das pessoas ordenado por prioridade
        individuos_priorities = map(lambda ind : int(ind.id), self.persons)

        #lista com os elementos repetidos tratada
        qtd_priorities = list(map(lambda ind : int(ind.split(';')[1]), list_corretct_priority))
        
        fitness = 0
        
        list_priority_convert = list(individuos_priorities)

        for ind in list_corretct_priority:
          (id_individuo_correto, priority_correct) = ind.split(';')
          
          # distancia dos itens levando em consideração a quantidade de elementos repetidos da posição
          diff_index = list_priority_convert.index(int(id_individuo_correto)) - int(priority_correct) - 1 - qtd_priorities.count(priority_correct)

          # penalidade_distance = 0

          if diff_index < 0:
            diff_index *= -1

          # if diff_index < 5 and diff_index > 0:
          #   penalidade_distance = 1
          
          # if diff_index >= 5 and diff_index < 10 and diff_index > 0:
          #   penalidade_distance = 1.5
          
          # if diff_index >= 10 and diff_index < 20 and diff_index > 0:
          #   penalidade_distance = 2
          
          # if diff_index >= 20 and diff_index < 30 and diff_index > 0:
          #   penalidade_distance = 3
          
          # if diff_index > 30 and diff_index > 0:
          #   penalidade_distance = 5

          fitness = fitness + diff_index 

        self.fitnessValue = round(fitness / len(list_priority_convert), 3)
        
      except:
        self.fitnessValue = 99999999999
    else:
      self.fitnessValue = 99999999999
      
      


      

