from selecion import selection
from Person import getAllPersons
from initial_population import initial_population
from utils import getSortedList, ordenaPopulacao
import numpy as np
from Person import getAtributesPerson
from crossover import crossover
from mutation import mutation
import matplotlib.pyplot as plt

# Não usar menos de 50 elementos pois quebra
QTD_INDIVIDUOS = 150
geracao = 0
TOTAL_GERACOES = 100

persons = getAllPersons() # pega todas as pessoas com as características
populacao = initial_population(persons, QTD_INDIVIDUOS) # população é composta de fórmulas

list_corretct_priority = getSortedList() # lista correta de priorização que será usada para avaliar a eficiencia da fórmula


best_members_each_generation = []

while geracao < TOTAL_GERACOES:
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
  print('A avaliação do individuo é ', round(individuo.fitnessValue, 3), 'e sua fórmula é ', individuo.formula.replace('|', ''))

list_do_alg = map(lambda ind : int(ind.id), populacao[0].persons)

list_fitness_value = list(map(lambda ind : int(ind.fitnessValue), populacao[:10]))


list_to_priorities_pie = list(map(lambda ind : int(ind.split(';')[0]), list_corretct_priority))
list_persons_to_pie = list(map(lambda ind : int(ind.id), populacao[0].persons))


plt.title("Melhores membros do resultado final")
plt.axis([0, 10, 0, len(list_to_priorities_pie)])
plt.plot(list_fitness_value)
plt.show()

plt.title("Fitness dos melhores membros de cada geração")
plt.plot(best_members_each_generation)
plt.show()

x = 1*np.array(range(len(list_to_priorities_pie)))

plt.plot( x, list_to_priorities_pie, 'go') # green bolinha
plt.plot( x, list_to_priorities_pie, 'k:', color='orange') # linha pontilha orange

plt.plot( x, list_persons_to_pie, 'r^') # red triangulo
plt.plot( x, list_persons_to_pie, 'k--', color='blue')  # linha tracejada azul

plt.axis([0, len(list_to_priorities_pie), 0, len(list_to_priorities_pie)])
plt.title("Listas comparativas")

plt.grid(True)
plt.xlabel("Pessoas")
plt.ylabel("Posição")
plt.show()

print('Evolução gerações: ', best_members_each_generation)
print('A melhor solução do algoritmo encontrada é: ', list_persons_to_pie)
print('A avaliação dela é: ', populacao[0].fitnessValue)


print('A lista ótima é: ', list_to_priorities_pie)


  
  






# avaliar populacao
# cruzar população
# mutar populaçao