import pygame
import random
import time
pygame.init()

screen_width = 500
screen_height = 500

def changeBackground(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))

pygame.display.set_caption("Recycle Marathon")
screen = pygame.display.set_mode([screen_width,screen_height])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RecycleMarathon/bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,80))
        self.rect = self.image.get_rect()

class Recycable(pygame.sprite.Sprite):
    def __init__(self,img):
        # super init function used to call to initialise the pygame.sprite.Sprite class
        # ensuring that recycable class is properly initialised as a sprite
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(50,80))
        self.rect = self.image.get_rect()

class Non_Recycable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RecycleMarathon/redbag.png")
        self.image = pygame.transform.scale(self.image,(50,80))
        self.rect = self.image.get_rect()


# list of images for recyclable items
images = ["C:\Users/44779\OneDrive\Documents\JetLearn\Pro Game Dev\RecycleMarathon\paperbag.png" , "C:\Users\44779\OneDrive\Documents\JetLearn\Pro Game Dev\RecycleMarathon\pencil.png" , "C:\Users\44779\OneDrive\Documents\JetLearn\Pro Game Dev\RecycleMarathon\wodenbox.png"  ]

# create sprite groups
item_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group() 