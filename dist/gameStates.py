import variables
import pygame
import os

def restartGame():
    variables.setPcTool("q")
    variables.setPlayerTool("q")
    variables.setSelected(False)
    variables.setEnded(False)
    variables.setCheckTime(False)
    variables.setFade(255)

def checkGame():
    variables.setTotalPlayed(variables.getTotalPlayed()+1)
    playerTool = variables.getPlayerTool()
    pcTool = variables.getPcTool()
    drawSound = pygame.mixer.Sound(os.path.join("media","draw.wav"))
    winSound = pygame.mixer.Sound(os.path.join("media","win.wav"))
    loseSound = pygame.mixer.Sound(os.path.join("media","lose.wav"))
    if(playerTool == pcTool):
        variables.setEnded("d")
        drawSound.play()
    if(playerTool == "r" and pcTool == "p"):
        variables.setEnded("l")
        variables.setPcWon(variables.getPcWon()+1)
        loseSound.play()
    if(playerTool == "p" and pcTool == "s"):
        variables.setEnded("l")
        variables.setPcWon(variables.getPcWon()+1)
        loseSound.play()
    if(playerTool == "s" and pcTool == "r"):
        variables.setEnded("l")
        variables.setPcWon(variables.getPcWon()+1)
        loseSound.play()
    if(playerTool == "r" and pcTool == "s"):
        variables.setEnded("w")
        variables.setPlayerWon(variables.getPlayerWon()+1)
        winSound.play()
    if(playerTool == "p" and pcTool == "r"):
        variables.setEnded("w")
        variables.setPlayerWon(variables.getPlayerWon()+1)
        winSound.play()
    if(playerTool == "s" and pcTool == "p"):
        variables.setEnded("w")
        variables.setPlayerWon(variables.getPlayerWon()+1)
        winSound.play()