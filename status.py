import labels_config

# baseDict = labels_config.status
baseLabels = labels_config.statusList

class Status():
  def __init__(self, statyChoose):
    self.name = baseLabels[statyChoose][0]
    self.description = baseLabels[statyChoose][1]
    self.tagNum = baseLabels[statyChoose][2]
    
  def setDifficulty(staty, statyChoose):
    staty.name = baseLabels[statyChoose][0]
    staty.description = baseLabels[statyChoose][1]
    staty.tagNum = baseLabels[statyChoose][2]
    return staty

  def __str__(self):
    return "status \n  name: " + self.name + "\n  description: " + self.description + "\n   tagNum: " + str(self.tagNum)

def statyTest():
  staty = Status(0)
  print(staty)
  staty = Status(1)
  print(staty)
  staty = Status(2)
  print(staty)
  staty = Status(3)
  print(staty)
  staty = Status(4)
  print(staty)
  staty = Status(5)
  print(staty)

def main():
  statyTest()

main()
