import operator

operacoes = {
  '+' : operator.add,
  '-' : operator.sub,
  '*' : operator.mul,
  '/' : operator.truediv,
  '%' : operator.mod,
  '^' : operator.xor,
}

class Formula:
  def __init__(self, formula):
    self.formula = formula
    self.ordenatePersons = []
    self.fitnessValue = None

  def calculePersonAtribute(self, person):
    # aqui vai operar o calculo
    return self

