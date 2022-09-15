playerWon = 0
pcWon = 0
pcTool = None
playerTool = None
selected = None
ended = None
checkTime = None
fade = None
totalPlayed = 0

def setTotalPlayed(value):
    global totalPlayed
    totalPlayed = value
def getTotalPlayed():
    return totalPlayed

def setPlayerWon(value):
    global playerWon
    playerWon = value
def getPlayerWon():
    return playerWon

def setPcWon(value):
    global pcWon
    pcWon = value
def getPcWon():
    return pcWon

def setPcTool(value):
    global pcTool
    pcTool = value
def getPcTool():
    return pcTool

def setPlayerTool(value):
    global playerTool
    playerTool = value
def getPlayerTool():
    return playerTool

def setSelected(value):
    global selected
    selected = value
def getSelected():
    return selected

def setEnded(value):
    global ended
    ended = value
def getEnded():
    return ended

def setCheckTime(value):
    global checkTime
    checkTime = value
def getCheckTime():
    return checkTime

def setFade(value):
    global fade
    fade = value
def getFade():
    return fade