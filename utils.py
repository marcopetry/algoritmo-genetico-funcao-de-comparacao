def getContentEmotions(individuo):
  f = open('database/emotions/labels_' + str(individuo) + '.txt')
  return f.readlines()

def getContentHeart(individuo):
  f = open('database/heartrate/hr_' + str(individuo) + '.txt')
  return f.readlines()
  