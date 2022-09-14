from sys import exit
import pygame
import os
import buttons
import centerText
import random

pygame.init()

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
ICONR = pygame.image.load(os.path.join("media", "iconRounded.png"))
pygame.display.set_caption("KPO - Kő Papír Olló")
pygame.display.set_icon(ICONR)

global run

FPS = 60

defaultButtonImage = pygame.image.load(os.path.join("media","defaultButton.png"))
defaultButtonImageHover = pygame.image.load(os.path.join("media","defaultButtonHover.png"))

defaultLongButtonImage = pygame.image.load(os.path.join("media","defaultLongButton.png"))
defaultLongButtonImageHover = pygame.image.load(os.path.join("media","defaultLongButtonHover.png"))

backgroundToolbar = pygame.image.load(os.path.join("media","backgroundToolbar.png"))

rockImage = pygame.image.load(os.path.join("media","rockImage.png"))
rockImageMedium = pygame.transform.scale(rockImage,(256,256))
rockImageSmall = pygame.transform.scale(rockImage,(70,70))
paperImage = pygame.image.load(os.path.join("media","paperImage.png"))
paperImageMedium = pygame.transform.scale(paperImage,(256,256))
paperImageSmall = pygame.transform.scale(paperImage,(70,70))
scissorsImage = pygame.image.load(os.path.join("media","scissorsImage.png"))
scissorsImageMedium = pygame.transform.scale(scissorsImage,(256,256))
scissorsImageSmall = pygame.transform.scale(scissorsImage,(70,70))

questionmarkImage = pygame.image.load(os.path.join("media","questionmarkImage.png"))
questionmarkImageMedium = pygame.transform.scale(questionmarkImage,(256,256))
questionmarkImageSmall = pygame.transform.scale(questionmarkImage,(70,70))

rockBtn = buttons.Button(15,515,70,70,defaultButtonImage,defaultButtonImageHover)
paperBtn = buttons.Button(100,515,70,70,defaultButtonImage,defaultButtonImageHover)
scissorsBtn = buttons.Button(185,515,70,70,defaultButtonImage,defaultButtonImageHover)

quitBtn = buttons.Button(885,525,100,50,defaultLongButtonImage,defaultLongButtonImageHover)
resetBtn = buttons.Button(770,525,100,50,defaultLongButtonImage,defaultLongButtonImageHover)

font = pygame.font.Font(os.path.join("media","font.ttf"), 16)

playerTool = False
pcTool = False

selected = False
ended = False

global start_time
start_time = False

global fade
fade = 255

def convertStringToImage(string):
    if(string == "r"): return rockImageMedium.copy()
    if(string == "p"): return paperImageMedium.copy()
    if(string == "s"): return scissorsImageMedium.copy()
    if(string == "q"): return questionmarkImageMedium.copy()
    return False

def restartGame():
    global pcTool
    global playerTool
    global selected
    global ended
    global start_time
    global fade
    pcTool = "q"
    playerTool = "q"
    selected = False
    ended = False
    start_time = False
    fade = 255

def checkGame():
    if(playerTool == pcTool):
        print("Döntetlen")
        restartGame()
    if(playerTool == "r" and pcTool == "p"):
        print("Vesztettél!")
        restartGame()
    if(playerTool == "p" and pcTool == "s"):
        print("Vesztettél!")
        restartGame()
    if(playerTool == "s" and pcTool == "r"):
        print("Vesztettél!")
        restartGame()
    if(playerTool == "r" and pcTool == "s"):
        print("Győztél!")
        restartGame()
    if(playerTool == "p" and pcTool == "r"):
        print("Győztél!")
        restartGame()
    if(playerTool == "s" and pcTool == "p"):
        print("Győztél!")
        restartGame()

def drawWindow():
    WIN.blit(backgroundToolbar,(0,0))
    global playerTool
    global pcTool
    global selected
    global ended
    global fade
    
    if rockBtn.draw(WIN) and selected == False:
        playerTool = "r"
        selected = True
    if paperBtn.draw(WIN) and selected == False:
        playerTool = "p"
        selected = True
    if scissorsBtn.draw(WIN) and selected == False:
        playerTool = "s"
        selected = True

    viewPlayerTool = convertStringToImage(playerTool)
    viewPcTool = convertStringToImage(pcTool)

    viewPcTool.set_alpha(fade)

    WIN.blit(viewPlayerTool,(64,500-256-128)) # player
    WIN.blit(viewPcTool,(1000-256-64,500-256-128)) # pc

    if selected == True and ended == False:

        fade = fade - 4
        
        if(fade <= 0):
            ended = True
            fade = 255
            pcTool = random.randint(0,2)
            if(pcTool == 0): pcTool = "r"
            if(pcTool == 1): pcTool = "p"
            if(pcTool == 2): pcTool = "s"

            global start_time
            start_time = pygame.time.get_ticks() + 2000
    

    if quitBtn.draw(WIN):
        pygame.quit()
        exit()
    if resetBtn.draw(WIN):
        print("Reset")

    centerText.render(WIN,"Kilépés",font,quitBtn.pos(),(200,200,200))
    centerText.render(WIN,"Reset",font,resetBtn.pos(),(200,200,200))

    WIN.blit(rockImageSmall,(rockBtn.cords()))
    WIN.blit(paperImageSmall,(paperBtn.cords()))
    WIN.blit(scissorsImageSmall,(scissorsBtn.cords()))    

    pygame.display.update()


def main():
    global playerTool
    global pcTool
    global selected
    global ended
    global start_time
    start_time = False
    selected = False
    playerTool = "q"
    pcTool = "q"
    ended = False
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if(selected):
            if(start_time - pygame.time.get_ticks()) <= 0: checkGame()
        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
