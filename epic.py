import labels_config

# baseDict = labels_config.epic
baseLabels = labels_config.epicList

class Epic():
  def __init__(self, epicNum):
    self.name = baseLabels[epicNum][0]
    self.examples = baseLabels[epicNum][1]
    self.tagNum = baseLabels[epicNum][2]
    
  def setDifficulty(epicy, epicNum):
    epicy.name = baseLabels[epicNum][0]
    epicy.examples = baseLabels[epicNum][1]
    epicy.tagNum = baseLabels[epicNum][2]
    return epicy

  def __str__(self):
    examplesList = "[\""
    for example in self.examples:
      examplesList += str(example)
      if(example != self.examples[-1]):
        examplesList += "\", \""
    examplesList += "\"]"
    return "epic \n  name: " + self.name + "\n  examples: " + examplesList + "\n   tagNum: " + str(self.tagNum)

def epicyTest():
  epicy = Epic(0)
  print(epicy)
  epicy = Epic(1)
  print(epicy)
  epicy = Epic(2)
  print(epicy)
  epicy = Epic(3)
  print(epicy)
  epicy = Epic(4)
  print(epicy)
  epicy = Epic(5)
  print(epicy)
  epicy = Epic(6)
  print(epicy)

def main():
  epicyTest()

main()
