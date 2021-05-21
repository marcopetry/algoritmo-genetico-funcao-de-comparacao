from Person import getAtributesPerson
from utils import getOperators, randomInt
import random

def randomOperator():
  operators = getOperators()
  return operators[int(random.randrange(0, len(operators) - 1, 1))] 

def randomAtribute():
  attr = getAtributesPerson()
  return attr[randomInt(0, len(attr) - 1)]

def mutation(mutation_members):
  operators = getOperators()

  for individuo in mutation_members:
    select_operator = randomOperator() # vai ser trocado da fórmula
    change_operator = randomOperator() # vai entrar na fórmula

    select_attr = randomAtribute()
    change_attr = randomAtribute()
    
    individuo.setFormula(individuo.formula.replace(select_operator, change_operator, 2).replace(select_attr, change_attr, 1).replace(str(randomInt(0, 5)), str(randomInt(0,5)))) # troca até dois operadores selecionados
  
  return mutation_members
  
