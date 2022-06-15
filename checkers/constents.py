import pygame
WIDTH = 500
HEIGHT = 500
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS #حجم المربع بتاع البورد
#RGB
BEIGE= (250,151,70)
GREY= (51,51,51)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(10,209,24)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'),(20,15))