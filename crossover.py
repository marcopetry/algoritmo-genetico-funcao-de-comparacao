import random
import re

from Person import getAtributesPerson

def crossover(crossover_members):
  cruzamento = 0
  qtd_cruzamentos = len(crossover_members)
  while cruzamento < qtd_cruzamentos: # cruzamento multipontos de corte      
    first_number_random = int(random.randrange(0, qtd_cruzamentos, 1))
    second_number_random = int(random.randrange(0, qtd_cruzamentos, 1))
    while first_number_random == second_number_random:
      second_number_random = int(random.randrange(0, qtd_cruzamentos, 1))
    
    first_member = crossover_members[first_number_random]
    second_member = crossover_members[second_number_random]

    attr_first_member = re.split('[+|*|/|^|-]', first_member.formula)
    attr_second_member = re.split('[+|*|/|^|-]', second_member.formula)

    array_controlador_qtd_atributos_trocados = []
    while len(array_controlador_qtd_atributos_trocados) < 2:
      number_random = int(random.randrange(0, len(attr_first_member) - 1, 1))      
      
      array_controlador_qtd_atributos_trocados.append(number_random)

      attr_first = attr_first_member[number_random]
      
      crossover_members[first_number_random].setFormula((crossover_members[first_number_random].formula.replace(attr_first_member[number_random], attr_second_member[number_random])))

      crossover_members[second_number_random].setFormula(crossover_members[second_number_random].formula.replace(attr_second_member[number_random], attr_first))

    cruzamento += 1
  return crossover_members
