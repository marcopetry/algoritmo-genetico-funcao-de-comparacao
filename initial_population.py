import utils
from Person import getAtributesPerson
from Formula import Formula
import random

def initial_population():
  populacao = []

  atributesPersons = getAtributesPerson()
  operators = ['+', '-', '*', '/', '^']
  # weights = [1, 2, 3, 4]
  formulas = []

  i = 0

  while i < 50:
    atributes = atributesPersons.copy()
    random.shuffle(atributes)
    formula = ''
    while len(atributes) > 0:
      sortNumber = random.randrange(0, len(atributes))
      atribute = atributes[sortNumber]
      atributes.remove(atribute)

      sortNumber = random.randrange(0, len(operators))
      if(len(atributes) > 0):
        formula = formula + atribute + operators[sortNumber]
      else:
        formula = formula + atribute

    formulas.append(Formula(formula))  
    i += 1
  return formulas



  



