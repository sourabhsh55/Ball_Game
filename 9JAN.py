import pygame as py
import random

#--
WIDTH =(700)
HEIGHT=(500)
FPS =(60)

#--
WHITE =(255,255,255)
BLACK =(0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE =(0,0,255)

class Player(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((40,40))
        self.image.fill(BLACK)
        py.draw.circle(self.image,GREEN,(20,20),20,0)
        self.rect = self.image.get_rect()
        self.rect.x =100
        self.rect.y =67
        self.speedx =3
        self.speedy =3


class Block(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((100,10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y =HEIGHT-40
        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = py.key.get_pressed()
        if keystate[py.K_LEFT]:
            self.speedx -=5
        if keystate[py.K_RIGHT]:
            self.speedx +=5
        self.rect.x += self.speedx
        if keystate[py.K_UP]:
            self.speedy -=5
        if keystate[py.K_DOWN]:
            self.speedy +=5
        self.rect.y += self.speedy
   #----------rigid-side-Walls------->
        if self.rect.right > WIDTH:
            self.rect.right =WIDTH
        if self.rect.left < 0:
            self.rect.left =0
        if self.rect.top <0 :
            self.rect.top =0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom =HEIGHT
        
        


#--
py.init()
screen = py.display.set_mode([WIDTH,HEIGHT])
py.display.set_caption('shoot')
clock = py.time.Clock()

all_sprites = py.sprite.Group()
all_blocks = py.sprite.Group()
player =Player()
block = Block()
all_sprites.add(player,block)
all_blocks.add(block)

#--
running = True
while running:
    clock.tick(FPS)
    for events in py.event.get():
        if events.type ==py.QUIT:
            running =False
    player.rect.x +=player.speedx
    player.rect.y +=player.speedy
   #----------rigid-side-Walls------->
    if player.rect.y>HEIGHT-50 or player.rect.y<0:
        player.speedy =player.speedy*(-1)
    if player.rect.x>WIDTH-50 or player.rect.x<0:
        player.speedx =player.speedx*(-1)
    #--===--===--===>>/...
    hits = py.sprite.spritecollide(player,all_blocks,False)
    if hits:
        player.speedy =player.speedy*(-1)
    #=============update,render..============>
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    py.display.flip()
    
    
    
    
    
    
    
    
    
py.quit()
quit()
            
