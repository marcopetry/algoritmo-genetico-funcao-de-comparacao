import random
import re
from utils import randomInt

from Person import getAtributesPerson

def crossover(crossover_members):
  cruzamento = 0
  qtd_cruzamentos = len(crossover_members)
  while cruzamento < qtd_cruzamentos: # cruzamento multipontos de corte      
    
    first_number_random = randomInt(0, qtd_cruzamentos - 2)
    second_number_random = randomInt(0, qtd_cruzamentos - 2)
    while first_number_random == second_number_random:
      second_number_random = randomInt(0, qtd_cruzamentos - 2)
    
    first_member_part = crossover_members[first_number_random].formula.split('|') # primeira corte do primeiro individuo
    second_member_part = crossover_members[second_number_random].formula.split('|') # segundo corte do segundo individuo

    # cruzamento um ponto de corte
    crossover_members[first_number_random].setFormula(first_member_part[0] + '|' + second_member_part[1])
    crossover_members[second_number_random].setFormula(second_member_part[0] + '|' + first_member_part[1])

    cruzamento += 1
    
  return crossover_members
