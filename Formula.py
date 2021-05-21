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
        if(len(atributes) > 0):
          formula = formula + atribute + operators[sortNumber]
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
    print(self.formula.replace('|', ''))
  
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
        individuos_priorities = map(lambda ind : int(ind.id), self.persons)
        
        fitness = 1

        list_priority_convert = list(individuos_priorities)

        for ind in list_corretct_priority:
          (id_individuo_correto, priority_correct) = ind.split(';')
          
          diff_index = list_priority_convert.index(int(id_individuo_correto)) - int(priority_correct) - 1

          fitness = fitness + (diff_index if diff_index > 0 else diff_index * -1)          

        self.fitnessValue = round(fitness / len(list_priority_convert), 3)
        
      except:
        self.fitnessValue = 99999999999
    else:
      self.fitnessValue = 99999999999
      
      


      

