import pygame
import os

def render(surface,text,font,pos,color):
    text = font.render(text,True,color)
    text_rect = text.get_rect(center=(pos[0]+pos[2]*0.5,pos[1]+pos[3]*0.5))
    surface.blit(text,text_rect)