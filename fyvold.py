from pygame import*

okno = display.set_mode((500,500))
game = True 

class KVADRAT(sprite.Sprite):
    def __init__(self, x):
        sprite.Sprite.__init__(self)
        self.image = Surface((80,140)) #прямоугольник
        self.rect = self.image.get_rect() #зона столкновений
        self.rect.x = x #местоположение квадрата
    def set_color(self,r,g,b):
        self.color = (r,g,b) #установка цвета
        self.image.fill(self.color) 
    def risuem(self):
        okno.blit(self.image, (self.rect.x, 200))

kv1 = KVADRAT(35) #создаем карточку
kv1.set_color(200,200,0) #задаем цвет карточки
while game: 
    for i in event.get():
        if i.type == QUIT: 
            game = False
        if i.type == MOUSEBUTTONDOWN: 
            if i.button == 1: 
                if kv1.rect.collidepoint(i.pos[0], i.pos[1]-200):
                    kv1.set_color(200,0,0)
    okno.fill((0,200,200)) 
    kv1.risuem() #рисуем карточку на экране
    display.update() 