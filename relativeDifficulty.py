import labels_config

# baseDict = labels_config.relativeDifficulty
baseLabels = labels_config.relDiffList

class RelativeDifficulty():
  def __init__(self, difficulty):
    self.icon = baseLabels[difficulty][0]
    self.description = baseLabels[difficulty][1]
    self.tagNum = baseLabels[difficulty][2]
    
  def setDifficulty(relDiff, difficulty):
    relDiff.icon = baseLabels[difficulty][0]
    relDiff.description = baseLabels[difficulty][1]
    relDiff.tagNum = baseLabels[difficulty][2]
    return relDiff

  def __str__(self):
    return "relativeDifficulty \n  icon: " + self.icon + "\n  description: " + self.description + "\n   tagNum: " + str(self.tagNum)

def relDiffTest():
  relDiff = RelativeDifficulty(0)
  print(relDiff)
  relDiff = RelativeDifficulty(1)
  print(relDiff)
  relDiff = RelativeDifficulty(2)
  print(relDiff)
  relDiff = RelativeDifficulty(3)
  print(relDiff)
  relDiff = RelativeDifficulty(4)
  print(relDiff)
  relDiff = RelativeDifficulty(5)
  print(relDiff)
  relDiff = RelativeDifficulty(6)
  print(relDiff)

def main():
  relDiffTest()

main()
