from pygame import *

'''Необходимые классы'''



#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) 
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
racket = Player('рокетка.png', 100, 500, 65 , 65, 200)
racket_2 = Player('рокетка.png', 100, 400, 65 , 65, 200)
ball = GameSprite('мяч.png', 100, 400, 65 , 65, 65)

#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (100,0,0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (100,0,0))
while game:
    racket.reset()
    racket.update()
    racket_2.reset()
    racket_2.update()
    for e in event.get():
       if e.type == QUIT:
           game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y += -1
    if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket_2, ball):
        speed_x += -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    display.update()
    clock.tick(FPS)


