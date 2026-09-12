'''
import load_players
import random
import copy

matchStatus = {"player1": {"name": "", "stats": {"serve": {"aces": 0, "doubleFaults": 0, "firstServe": 0.0, "firstServePoints": 0.0, "secondServePoints": 0.0, "servePointsWon": 0.0, "breakPoint": 0.0, "serviceGamesWon": 0.0}, "return": {"firstReturnPoints": 0.0, "secondReturnPoints": 0.0, "returnGamesWon": 0.0, "breakPointConversion": 0.0, "returnPointsWon": 0.0}}, "score": {"firstSet": [], "secondSet": [], "thirdSet": []}}, "player2": {"name": "", "stats": {"serve": {"aces": 0, "doubleFaults": 0, "firstServe": 0.0, "firstServePoints": 0.0, "secondServePoints": 0.0, "servePointsWon": 0.0, "breakPoint": 0.0, "serviceGamesWon": 0.0}, "return": {"firstReturnPoints": 0.0, "secondReturnPoints": 0.0, "returnGamesWon": 0.0, "breakPointConversion": 0.0, "returnPointsWon": 0.0}}, "score": {"firstSet": [], "secondSet": [], "thirdSet": []}}, "setCounter": "", "server": "player1"}

mockWTAPlayer1 = load_players.PlayerStats("Coco Gauff", load_players.WTAServer("26", "93", "151", "62.2", "72.6", "41.4", "60.8", "55.8", "73.6"), load_players.WTAReturner("26", "43.3", "54.8", "42.6", "53.2", "47.6"))
mockWTAPlayer2 = load_players.PlayerStats("Aryna Sabalenka", load_players.WTAServer("36", "11", "59", "63.6", "68.2", "50.8", "61.8", "66.1", "77.5"), load_players.WTAReturner("36", "40.2", "61.6", "44.5", "51.3", "48.2"))

class WTAMatch:
  def __init__(self, player1Stats, player2Stats):
    self.score = Score()
    self.bestOf = 3
    self.tieBreakFinal = True
    self.player1Stats = player1Stats
    self.player2Stats = player2Stats
'''

import labels_config

class TaskData(taskData)
