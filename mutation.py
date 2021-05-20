from utils import getOperators
import random

def randomOperator():
  operators = getOperators()
  return int(random.randrange(0, len(operators) - 1, 1))

def mutation(mutation_members):
  operators = getOperators()

  for individuo in mutation_members:
    select_operator = randomOperator() # vai ser trocado da fórmula
    change_operator = randomOperator() # vai entrar na fórmula
    while select_operator == change_operator:
      change_operator = randomOperator() # vai entrar na fórmula
    
    individuo.setFormula(individuo.formula.replace(operators[select_operator], operators[change_operator], 2)) # troca até dois operadores selecionados
  
  return mutation_members
  
