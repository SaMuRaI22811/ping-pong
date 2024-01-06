from pygame import *
from random import randint
from time import time as timer
mixer.init()
mw = display.set_mode((1500,800))
background = transform.scale(image.load('back.png'),(1500,800))
game_run = True
clock = time.Clock()
mixer.music.load('Geometry_Dash_-_Electrodynamix_63895597.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.06)
move_mode = 1
movey = 0
spdbal = 3
fix_speed = 0
class Roketka(sprite.Sprite):
    def __init__(self,images,x_raz,y_raz,x,y):
        super().__init__()
        self.x_raz = x_raz
        self.y_raz = y_raz
        self.images = transform.scale(image.load(images),(x_raz,y_raz))
        self.rect = self.images.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        mw.blit(self.images,(self.rect.x,self.rect.y))
class Myach(sprite.Sprite):
    def __init__(self,images,x_raz,y_raz,x,y):
        super().__init__()
        self.x_raz = x_raz
        self.y_raz = y_raz
        self.images = transform.scale(image.load(images),(x_raz,y_raz))
        self.rect = self.images.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        mw.blit(self.images,(self.rect.x,self.rect.y))
    def moving(self):
        if move_mode == 1:
            self.rect.x += spdbal
        if move_mode == 0:
            self.rect.x -= spdbal
        if movey == 1:
            self.rect.y -= spdbal
        if movey == 2:
            self.rect.y += spdbal
rok1 = Roketka('rok.png',100,150,10,400)
rok2 = Roketka('rok.png',100,150,1390,400)
myach = Myach('myach.png',75,75,750,400)
sec = 2
start = timer()
while game_run:
    for i in event.get():
        if i.type == QUIT:
            game_run = False
    mw.blit(background,(0,0))
    rok1.update()
    rok2.update()
    myach.update()
    myach.moving()
    keys = key.get_pressed()
    if keys[K_w] and rok1.rect.y > 0:
        rok1.rect.y -= 4
    if keys[K_s] and rok1.rect.y < 650:
        rok1.rect.y += 4
    if keys[K_UP] and rok2.rect.y > 0:
        rok2.rect.y -= 4
    if keys[K_DOWN] and rok2.rect.y < 650:
        rok2.rect.y += 4
    if myach.rect.x > 1500 or myach.rect.x < 0:
        mw.fill((0,0,0))
        mixer.music.set_volume(0)
        game_run = False
    if sprite.collide_rect(rok2,myach):
        move_mode = 0
        if myach.rect.y < rok2.rect.y and myach.rect.x < rok2.rect.x-12:
            movey = 1
        if myach.rect.y > rok2.rect.y+50 and myach.rect.x > rok2.rect.x-12:
            movey = 2
        if myach.rect.y > rok2.rect.y+35 and myach.rect.y < rok2.rect.y+50:
            movey = 0
            sec -= 1
    if sprite.collide_rect(rok1,myach):
        move_mode = 1
        if myach.rect.y < rok1.rect.y+20 and myach.rect.x < rok1.rect.x-12:
            movey = 1
        if myach.rect.y > rok1.rect.y+50 and myach.rect.x > rok1.rect.x-12:
            movey = 2
        if myach.rect.y > rok1.rect.y+35 and myach.rect.y < rok1.rect.y+50:
            movey = 0
            sec -= 1
    if sec < 0:
        movey = randint(1,2)
        sec = 2
        spdbal += 2
    if sec < 2 and movey != 0:
        sec = 2
    if myach.rect.y < 0:
        movey = 2
    if myach.rect.y > 725:
        movey = 1
    '''start = timer()
    if movey == 0:
        end = timer()
        if int(end-start) == sec:
            movey = randint(1,2)'''
    end = timer()
    if int(end-start) >= 20 and fix_speed < 1:
        spdbal += 1
        fix_speed += 1
    if int(end-start) >= 50 and fix_speed < 2:
        spdbal += 1
        fix_speed += 1
    print(spdbal)
    display.update()
    clock.tick(90)