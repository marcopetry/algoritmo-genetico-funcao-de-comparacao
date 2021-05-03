from utils import getContentEmotions, getContentHeart

def getAllPersons():  
  persons = []
  i = 0
  # Pega todas as informações que importam das pessoas e trata
  while i < 60:
    linesEmotions = getContentEmotions(i + 1)
    ignoreLine = True
    qtdEmotions = 0
    qtdFramesMotion = 0
    for line in linesEmotions:
      if(ignoreLine):
        ignoreLine = False
        continue
      
      qtdEmotions += 1
      infosEmotions = line.replace('\n', '').split(',')
      qtdFramesMotion = qtdFramesMotion + int(infosEmotions[1]) - int(infosEmotions[0])
    
    linesHeartbeats = getContentHeart(i + 1)

    totalCountHeartBeats = 0
    totalHeartbeats = 0
    minHeartBeat = 9999
    maxHeartBeat = 0

    for line in linesHeartbeats:
      line = line.replace('\n', '').split(',')
      heartBeat = int(line[1])
      totalCountHeartBeats += 1
      totalHeartbeats += heartBeat
      if(heartBeat > maxHeartBeat):
        maxHeartBeat = heartBeat

      if(heartBeat < minHeartBeat):
        minHeartBeat = heartBeat

    person = Person(i + 1, totalHeartbeats, maxHeartBeat, minHeartBeat, totalHeartbeats / totalCountHeartBeats, 0, qtdEmotions, qtdFramesMotion)
    persons.append(person)

    i += 1
  return persons


def getAtributesPerson():
  return ['totalHeartbeat', 'maxHearbeat', 'minHearbeat', 'mediaHeartbeat', 'desvioPadraoHeartbeat', 'amountEmotion', 'amountFramesEmotion']

class Person:
  def __init__(self, id, totalHeartbeat, maxHearbeat, minHearbeat, mediaHeartbeat, desvioPadraoHeartbeat, amountEmotion, amountFramesEmotion):
    self.id = id
    self.totalHeartbeat = totalHeartbeat
    self.maxHearbeat = maxHearbeat 
    self.minHearbeat = minHearbeat
    self.mediaHeartbeat = mediaHeartbeat
    self.desvioPadraoHeartbeat = desvioPadraoHeartbeat
    self.amountEmotion = amountEmotion
    self.amountFramesEmotion = amountFramesEmotion
    self.priority = None
  
  def getPerson(self):
    return self

  def setPriority(self, priority):
    self.priority = priority

  def printPerson(self):
    print('Total batimentos ' + str(self.totalHeartbeat))
    print('Max batimentos ' + str(self.maxHearbeat))
    print('Min batimentos ' + str(self.minHearbeat))
    print('Média batimentos ' + str(self.mediaHeartbeat))
    print('Desvio padrão batimentos ' + str(self.desvioPadraoHeartbeat))
    print('Total emoções ' + str(self.amountEmotion))
    print('Total de frames de emoções ' + str(self.amountFramesEmotion))
