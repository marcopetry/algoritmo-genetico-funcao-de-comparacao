import random
from utils import randomInt

def selection(populacao):
  ten_best_members = populacao[:10] # elitismo, permanecer 10 melhores membros
  mutation_members = populacao[len(populacao) - 10:] # piores membros sofrerão mutação

  crossover_members = []

  array_ref_member_crossover = []
  count = 0


  # aplicada estratégia do torneio
  while count < int(len(populacao) / 2): # seleciona pelo método torneio metade dos melhores membros com as melhores aptidões
    number = randomInt(10, int((len(populacao) / 2)))
    
    array_ref_member_crossover.append(number)

    count += 1
  
  for index_member in array_ref_member_crossover:
    crossover_members.append(populacao[index_member])
  
  return ten_best_members, crossover_members, mutation_members
  

