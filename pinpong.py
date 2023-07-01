import pygame as pg
import random
pg.init()
win_width, win_hight = 800,600
window = pg.display.set_mode((win_width, win_hight))
pg.display.set_caption("пинг понг")
score1 = 0
score2 = 0
class GameSprite:
    def __init__ (self, image, x,y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image),(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def control1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s] and self.rect.y < 600-250:
            self.rect.y += self.speed
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def control2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] and self.rect.y < 600-250:
            self.rect.y += self.speed
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def move (self):
        global x2,y2,player1, player2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(player2,self):
            x2 =-5
        if pg.sprite.collide_rect(player1,self):
            x2 =5
        if self.rect.y < 0:
            y2 = 5
        if self.rect.y > 525:
            y2 = -5
x2,y2 = 5,5
def check_score():
    global srore1, score2
    if srore >= 5 or score2 >=5:
        return True
    return False

back = GameSprite("download.jpg",0,0,800,600,0)
player1 = Player("download (2).jpg",0,300,20,250,3)
player2 = Player("download (2).jpg",780,300,20,250,3)
ball = Ball("мяч.png", 450,275,25,25,5)
win = "win.jpg"
game=True
miss_enemy = 0
score = 0
count_animation = 0
while game: 
    pg.time.Clock().tick(144)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    if ball.rect.x < 0:
        score1 +=1
        ball.rect.x = 400
    if score1 > 5:
        GameOver = "lose.png"
        game = False
    if ball.rect.x > 800:
        score2 +=1
        ball.rect.x = 400
    if score2 >= 5:
        GameOver = "lose.png"
        game = False
    back.reset()
    label = pg.font.SysFont("Aerial",25). render(f"Score pl1: {score1}", True, 'white')
    window.blit(label,(20,20))
    label = pg.font.SysFont("Aerial",25). render(f"Score pl2: {score2}", True, 'white')
    window.blit(label,(580,20))
    player1.reset()
    player1.control1()
    player2.control2()
    if score1 > 5:
        player1 = win
        GameOver = "win.png"
    if score2 > 5:
        player2 = win
        GameOver = "win.png"
    player2.reset()
    ball.reset()
    ball.move()
    pg.display.flip()
