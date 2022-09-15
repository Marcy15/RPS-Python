from sys import exit
import pygame
import os
import buttons
import centerText
import random
import gameStates
import variables

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
fontMid = pygame.font.Font(os.path.join("media","font.ttf"), 20)
fontBig = pygame.font.Font(os.path.join("media","font.ttf"),42)

def convertStringToImage(string):
    if(string == "r"): return rockImageMedium.copy()
    if(string == "p"): return paperImageMedium.copy()
    if(string == "s"): return scissorsImageMedium.copy()
    if(string == "q"): return questionmarkImageMedium.copy()
    return False

def drawWindow():
    WIN.blit(backgroundToolbar,(0,0))
    
    if rockBtn.draw(WIN) and variables.getSelected() == False:
        variables.setPlayerTool("r")
        variables.setSelected(True)
    if paperBtn.draw(WIN) and variables.getSelected() == False:
        variables.setPlayerTool("p")
        variables.setSelected(True)
    if scissorsBtn.draw(WIN) and variables.getSelected() == False:
        variables.setPlayerTool("s")
        variables.setSelected(True)

    viewPlayerTool = convertStringToImage(variables.getPlayerTool())
    viewPcTool = convertStringToImage(variables.getPcTool())

    viewPcTool.set_alpha(variables.getFade())

    if(variables.getEnded() == "d"):
        centerText.render(WIN,"Döntetlen!",fontBig,(0,0,1000,500),(41, 143, 171))
    if(variables.getEnded() == "w"):
        centerText.render(WIN,"Nyertél!",fontBig,(0,0,1000,500),(126, 196, 51))
    if(variables.getEnded() == "l"):
        centerText.render(WIN,"Vesztettél!",fontBig,(0,0,1000,500),(222, 75, 53))

    WIN.blit(viewPlayerTool,(64,500-256-128)) # player
    WIN.blit(viewPcTool,(1000-256-64,500-256-128)) # pc

    if variables.getSelected() == True and variables.getEnded() == False:

        variables.setFade(variables.getFade() - 4)
        
        if(variables.getFade() <= 0):
            variables.setEnded(True)
            variables.setFade(255)
            tempPcTool = random.randint(0,2)
            if(tempPcTool == 0): tempPcTool = "r"
            if(tempPcTool == 1): tempPcTool = "p"
            if(tempPcTool == 2): tempPcTool = "s"
            variables.setPcTool(tempPcTool)

            variables.setCheckTime(pygame.time.get_ticks() + 2000)

            gameStates.checkGame()
    

    if quitBtn.draw(WIN):
        pygame.quit()
        exit()
    if resetBtn.draw(WIN):
        variables.setTotalPlayed(0)
        variables.setPcWon(0)
        variables.setPlayerWon(0)
        gameStates.restartGame()
        return

    centerText.render(WIN,"Kilépés",font,quitBtn.pos(),(230,230,230))
    centerText.render(WIN,"Reset",font,resetBtn.pos(),(230,230,230))

    #pygame.draw.rect(WIN,(0,0,0),pygame.Rect(270,515,70,70))
    #pygame.draw.rect(WIN,(0,0,0),pygame.Rect(685,515,70,70))
    #pygame.draw.rect(WIN,(100,100,10),pygame.Rect(340,515,345,70))


    kd = "-"
    if(variables.getTotalPlayed() != 0):
        kd = variables.getPlayerWon()/variables.getTotalPlayed()*100
        kd = str(int(kd)) + "%"

    centerText.render(WIN,str(variables.getPlayerWon()),fontBig,(270,515,70,70),(126, 196, 51))
    centerText.render(WIN,str(variables.getPcWon()),fontBig,(685,515,70,70),(222, 75, 53))
    centerText.render(WIN,"Nyerési arány: "+kd,fontMid,(340,515,345,50),(230,230,230))
    centerText.render(WIN,"Lejátszott játékok: "+str(variables.getTotalPlayed()),fontMid,(340,535,345,70),(230,230,230))

    WIN.blit(rockImageSmall,(rockBtn.cords()))
    WIN.blit(paperImageSmall,(paperBtn.cords()))
    WIN.blit(scissorsImageSmall,(scissorsBtn.cords()))    

    pygame.display.update()


def main():
    run = True
    gameStates.restartGame()
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if(variables.getSelected() == True):
            if variables.getCheckTime() != False and (variables.getCheckTime() - pygame.time.get_ticks()) <= 0:
                gameStates.restartGame()
        
        drawWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
