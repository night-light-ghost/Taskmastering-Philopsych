import labels_config

# baseDict = labels_config.satisfaction
baseLabels = labels_config.satisfactionList

class Satisfaction():
  def __init__(self, satisfactionNum):
    self.name = baseLabels[satisfactionNum][0]
    self.description = baseLabels[satisfactionNum][1]
    self.tagNum = baseLabels[satisfactionNum][2]
    
  def setDifficulty(satisfy, satisfactionNum):
    satisfy.name = baseLabels[satisfactionNum][0]
    satisfy.description = baseLabels[satisfactionNum][1]
    satisfy.tagNum = baseLabels[satisfactionNum][2]
    return satisfy

  def __str__(self):
    return "satisfaction \n  name: " + self.name + "\n  description: " + self.description + "\n   tagNum: " + str(self.tagNum)

def satisfyTest():
  satisfy = Satisfaction(0)
  print(satisfy)
  satisfy = Satisfaction(1)
  print(satisfy)
  satisfy = Satisfaction(2)
  print(satisfy)
  satisfy = Satisfaction(3)
  print(satisfy)
  satisfy = Satisfaction(4)
  print(satisfy)

def main():
  satisfyTest()

main()
