import re
import pygame

class Button():
    def __init__(self, x, y ,w,h, image, imageHover=False):
        self.image = pygame.transform.scale(image, (w, h))
        self.imageHover = imageHover
        if(imageHover != False):
            self.imageHover = pygame.transform.scale(imageHover, (w, h))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def pos(self):
        return self.rect
    def cords(self):
        return self.rect.topleft

    def draw(self, surface):
        action = False
        renderImage = self.image
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if(self.imageHover != False):
                renderImage = self.imageHover
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(renderImage, (self.rect.x, self.rect.y))

        return action