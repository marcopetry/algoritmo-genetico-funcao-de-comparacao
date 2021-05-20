from Person import getAtributesPerson
from Formula import Formula
from utils import getOperators

def initial_population(persons, qtd_individuos):
  formulas = []
  i = 0

  while i < qtd_individuos:
    formula = Formula(persons)
    formula.createFormula()
    formulas.append(formula)  
    i += 1
  return formulas



  



