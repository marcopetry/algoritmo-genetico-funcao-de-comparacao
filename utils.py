import random

def getContentEmotions(individuo):
  file = open('database/emotions/labels_' + str(individuo) + '.txt')
  return file.readlines()

def getContentHeart(individuo):
  file = open('database/heartrate/hr_' + str(individuo) + '.txt')
  return file.readlines()

def getSortedList():
  list = []
  file = open('database/priorities.txt')
  lines = file.readlines()

  for line in lines[2:]:
    list.append(line.replace('\n', ''))
  
  list.sort(reverse=False, key=lambda item : int(item.split(';')[1]))
  
  return list

def ordenaPopulacao(populacao):  
  populacao.sort(key=lambda ind : ind.fitnessValue) # ordena os individuos do melhor pro pior

def getOperators():
  return ['+', '-', '*', '/', '^']

def randomInt(begin = 0, end = 10):  
  return int(random.randrange(begin, end, 1))