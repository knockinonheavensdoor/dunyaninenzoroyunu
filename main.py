import pygame
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
dt = 0
pygame.init()
genislik, yukseklik = 800, 600
screen = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Ok Avcısı")
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
fonth = pygame.font.Font(None, 30)
fontg = pygame.font.Font(None, 120)
color = "white"
Frame = True
cnt = True
obj = []
ok = []
skor = 0
fps = 0
hiz = 300
sutun_yon = [[175, "yukari", 0], [325, "sol", 0], [475, "sag", 0], [625, "asagi", 0]]


class Nesne:
    def __init__(self, renk):
        self.renk = renk
        konum_yon = random.choice(sutun_yon)
        self.konum, self.yon = pygame.Vector2(konum_yon[0], 0), konum_yon[1]
    def ciz(self):
        if self.yon == "yukari":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 30, 60))
            pygame.draw.polygon(screen, self.renk, ((self.konum.x + 25, self.konum.y), (self.konum.x - 25, self.konum.y), (self.konum.x, self.konum.y-25)))

        elif self.yon == "sag":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 60, 30))
            pygame.draw.polygon(screen, self.renk, (((self.konum.x + 45, self.konum.y - 10), (self.konum.x + 45, self.konum.y + 40), (self.konum.x + 70, self.konum.y + 15))))
        elif self.yon == "sol":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 60, 30))
            pygame.draw.polygon(screen, self.renk, (((self.konum.x - 15, self.konum.y - 10), (self.konum.x - 15, self.konum.y + 40), (self.konum.x - 40, self.konum.y + 15))))
        elif self.yon == "asagi":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 30, 60))
            pygame.draw.polygon(screen, self.renk, ((self.konum.x + 25, self.konum.y + 60), (self.konum.x - 25, self.konum.y + 60), (self.konum.x, self.konum.y + 85)))


class Ok:
    def __init__(self, renk, yon):
        self.renk = renk
        self.yon = yon
        for i in sutun_yon:
            if i[1] == yon:
                self.konum = pygame.Vector2(i[0], 500)
    def ciz(self):
        if self.yon == "yukari":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 30, 60))
            pygame.draw.polygon(screen, self.renk, ((self.konum.x + 25, self.konum.y), (self.konum.x - 25, self.konum.y), (self.konum.x, self.konum.y-25)))

        elif self.yon == "sag":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 60, 30))
            pygame.draw.polygon(screen, self.renk, (((self.konum.x + 45, self.konum.y - 10), (self.konum.x + 45, self.konum.y + 40), (self.konum.x + 70, self.konum.y + 15))))
        elif self.yon == "sol":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 60, 30))
            pygame.draw.polygon(screen, self.renk, (((self.konum.x - 15, self.konum.y - 10), (self.konum.x - 15, self.konum.y + 40), (self.konum.x - 40, self.konum.y + 15))))
        elif self.yon == "asagi":
            pygame.draw.rect(screen, self.renk, pygame.Rect(self.konum.x - 15, self.konum.y, 30, 60))
            pygame.draw.polygon(screen, self.renk, ((self.konum.x + 25, self.konum.y + 60), (self.konum.x - 25, self.konum.y + 60), (self.konum.x, self.konum.y + 85)))


while Frame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Frame = False
    if cnt:
        screen.fill("white")
        skoryazi = fonth.render(f"Skor: {skor} Hiz: {hiz} Sıklık (o/Ft): 1 / {70 - (hiz // 50)}", True, "red")
        screen.blit(skoryazi, (10, 10))
        Ok("red", "sol").ciz(), Ok("red", "sag").ciz(), Ok("red", "yukari").ciz(), Ok("red", "asagi").ciz()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            for i in obj:
                if i.konum.x == 325:
                    if 490 < i.konum.y < 540:
                        obj.remove(i)
                        skor += 5
                        hiz += 10
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            for i in obj:
                if i.konum.x == 475:
                    if 490 < i.konum.y < 540:
                        obj.remove(i)
                        skor += 5
                        hiz += 10
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            for i in obj:
                if i.konum.x == 175:
                    if 490 < i.konum.y < 570:
                        obj.remove(i)
                        skor += 5
                        hiz += 10
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            for i in obj:
                if i.konum.x == 625:
                    if 490 < i.konum.y < 570:
                        obj.remove(i)
                        skor += 5
                        hiz += 10
        if len(obj) <= 10:
            if random.randint(0, 70 - (hiz // 50)) == 1:
                a = Nesne("blue")
                for j in sutun_yon:
                    if a.yon == j[1] and j[2] == 0:
                        j[2] = 3
                        obj += [a]
                    if j[2] != 0:
                        pass
                for k in sutun_yon:
                    if k[2] != 0:
                        k[2] -= 1
        for i in obj:
            i.konum.y += hiz * dt
            i.ciz()
            if i.konum.y > screen.get_height():
                cnt = False
        pygame.display.flip()
    else:
        screen.fill("black")
        go = fontg.render("OYUN BITTI", True, "red")
        screen.blit(go, (100, 100))
    pygame.display.flip()
    dt = clock.tick(144) / 1000
pygame.quit()