from selecion import selection
from Person import getAllPersons
from initial_population import initial_population
from utils import getSortedList, ordenaPopulacao
import numpy as np
from Person import getAtributesPerson
from crossover import crossover
from mutation import mutation
import matplotlib.pyplot as plt

QTD_INDIVIDUOS = 150
persons = getAllPersons() # pega todas as pessoas com as características
populacao = initial_population(persons, QTD_INDIVIDUOS) # população é composta de fórmulas

list_corretct_priority = getSortedList() # lista correta de priorização que será usada para avaliar a eficiencia da fórmula

geracao = 0
total_geracoes = 500

best_members_each_generation = []

while geracao < total_geracoes:
  geracao += 1


  for individuo in populacao:
    individuo.fitness(list_corretct_priority) # calculo da fitness  
    if individuo.fitnessValue == 0: 
      print('Solução ótima', individuo.formula)
      break
    
  ordenaPopulacao(populacao)

  best_members_each_generation.append(populacao[0].fitnessValue)
  (ten_best_members, crossover_members, mutation_members) = selection(populacao)

  crossover_members= crossover(crossover_members)
  mutation_members = mutation(mutation_members)

  populacao = list(np.hstack((ten_best_members, crossover_members, mutation_members)).ravel())

ordenaPopulacao(populacao)
for individuo in populacao[:10]: # print os 10 melhores itens
  print('A avaliação do individuo é ', round(individuo.fitnessValue, 3), 'e sua fórmula é ', individuo.formula)

list_do_alg = map(lambda ind : int(ind.id), populacao[0].persons)


print(best_members_each_generation)
plt.plot(best_members_each_generation)
plt.title("Melhores membros de cada geração")
plt.show()
# print('A melhor solução do algoritmo encontrada é: ', list(list_do_alg))
# print('A avaliação dela é: ', populacao[0].fitnessValue)


# print('A lista ótima é: ', list_corretct_priority)

  # 100000 individuos acertou 6

  
  






# avaliar populacao
# cruzar população
# mutar populaçao