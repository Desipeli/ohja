import pygame
import math
import random


class Peli:

    def __init__(self):      
        pygame.init()
        self.naytto = pygame.display.set_mode((1200,800))
        self.lataa_kuvat()
        self.pelaaja = self.hahmo(self.kuvat[0], (350,250), 3)
        
        #Muuttujat liikkumiseen
        self.nopeus = 5
        self.ylos = False
        self.alas = False
        self.vasemmalle = False
        self.oikealle = False

        #Testijuttui
        if True:
            self.aave = self.hahmo(self.kuvat[1],(300,600), 1)
            self.aave2 = self.hahmo(self.kuvat[1],(100,300), 1)
            self.aave3 = self.hahmo(self.kuvat[1],(700,10), 1)
            self.aaveet = [self.aave, self.aave2, self.aave3]
        else:
            self.aave3 = self.hahmo(self.kuvat[1],(700,10), 1)
            self.aaveet = [self.aave3]


        self.kello = pygame.time.Clock()
        self.pelaa()
        
        

    def lataa_kuvat(self):
        self.kuvat = []
        for nimi in ["robo", "hirvio", "kolikko", "ovi"]:
            try:
                self.kuvat.append(pygame.image.load(nimi + ".png"))
            except:
                print(f"ongelma kuvan {nimi} lataamisessa")

    class hahmo:
        def __init__(self, kuva, sijainti: tuple, hp: int) -> None:
            self.kuva = kuva
            self.sijainti = sijainti    # (x,y)
            self.hp = hp
            self.rect = pygame.Rect(sijainti[0], sijainti[1],50,50)
            self.vauhti = (0,0)
            self.max_vauhti = random.randint(20,50)



    def liiku(self):
        if self.ylos:
            self.pelaaja.sijainti = self.pelaaja.sijainti[0], self.pelaaja.sijainti[1] - self.nopeus
        if self.alas:
            self.pelaaja.sijainti = self.pelaaja.sijainti[0], self.pelaaja.sijainti[1] + self.nopeus
        if self.vasemmalle:
            self.pelaaja.sijainti = self.pelaaja.sijainti[0] - self.nopeus, self.pelaaja.sijainti[1]
        if self.oikealle:
            self.pelaaja.sijainti = self.pelaaja.sijainti[0] + self.nopeus, self.pelaaja.sijainti[1]
    
    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
        self.liiku()

        

    
    def liikuta_aaveita_alkuperainen(self):
        #for a in self.aaveet:
        #    if a.sijainti[0] > self.pelaaja.sijainti[0]:
        #        a.sijainti = a.sijainti[0] - 1, a.sijainti[1]
        #    if a.sijainti[0] < self.pelaaja.sijainti[0]:
        #        a.sijainti = a.sijainti[0] + 1, a.sijainti[1]
        #    if a.sijainti[1] > self.pelaaja.sijainti[1]:
        #        a.sijainti = a.sijainti[0], a.sijainti[1] - 1
        #    if a.sijainti[1] < self.pelaaja.sijainti[1]:
        #        a.sijainti = a.sijainti[0], a.sijainti[1] + 1
        for a in self.aaveet:
            x_erotus = a.sijainti[0] - self.pelaaja.sijainti[0] # plus = pelaaja vasemmalla
            y_erotus = a.sijainti[1] - self.pelaaja.sijainti[1] # plus = pelaaja ylhäällä
            
            #if x_erotus == 0:
            #    x_norm = 0
            #else: x_norm = x_erotus/abs(x_erotus) * (-1)
            #if y_erotus == 0:
            #    y_norm = 0
            #else: y_norm = y_erotus/abs(y_erotus) * (-1)

            x_norm = math.copysign(1,-x_erotus)
            y_norm = math.copysign(1,-y_erotus)

            a.sijainti = a.sijainti[0] + x_norm * abs(x_erotus)/100 , a.sijainti[1] + y_norm * abs(y_erotus)/100

            for b in self.aaveet:
                if a != b:
                    x_erotus = a.sijainti[0] - b.sijainti[0] 
                    y_erotus = a.sijainti[1] - b.sijainti[1]
                    x_norm = math.copysign(1,x_erotus)
                    y_norm = math.copysign(1,y_erotus)     
                    a.sijainti = a.sijainti[0] + x_norm / abs(x_erotus)*10 , a.sijainti[1] + y_norm / abs(y_erotus)*10



    def liikuta_aaveita2(self):

        for a in self.aaveet:
            x_erotus = a.sijainti[0] - self.pelaaja.sijainti[0] # plus = pelaaja vasemmalla
            y_erotus = a.sijainti[1] - self.pelaaja.sijainti[1] # plus = pelaaja ylhäällä

            etaisyys_pelaajaan = math.sqrt((a.sijainti[0] - self.pelaaja.sijainti[0])**2 + (a.sijainti[1] - self.pelaaja.sijainti[1])**2)
            print(etaisyys_pelaajaan)

            x_norm = math.copysign(1,-x_erotus)
            y_norm = math.copysign(1,-y_erotus)
            
            a.vauhti = a.vauhti[0]  - x_erotus/20 , a.vauhti[1]  - y_erotus/20


            for b in self.aaveet:
                if a != b:
                    if a.sijainti[0] != b.sijainti[0]: 
                        x_erotus = a.sijainti[0] - b.sijainti[0] 
                    if a.sijainti[1] != b.sijainti[1]:
                        y_erotus = a.sijainti[1] - b.sijainti[1]
                    x_norm = math.copysign(1,x_erotus)
                    y_norm = math.copysign(1,y_erotus)     

                    a.vauhti = a.vauhti[0] + x_norm * (5/x_erotus)**2 , a.vauhti[1] + y_norm * (5/y_erotus)**2
            max_vauhti = a.max_vauhti

            if a.vauhti[0] > max_vauhti:
                a.vauhti = max_vauhti, a.vauhti[1]
            if a.vauhti[1] > max_vauhti:
                a.vauhti = a.vauhti[0], max_vauhti
            if a.vauhti[0] < -max_vauhti:
                a.vauhti = -max_vauhti, a.vauhti[1]
            if a.vauhti[1] < -max_vauhti:
                a.vauhti = a.vauhti[0], -max_vauhti
            a.sijainti = a.sijainti[0] + a.vauhti[0]/20, a.sijainti[1] + a.vauhti[1]/20
            #### LASKE ETÄISYYS, EI VAIN X tai Y etä=  sqrt(x**2 +y**2)

    def liikuta_aaveita(self):

        for a in self.aaveet:
            x_erotus = a.sijainti[0] - self.pelaaja.sijainti[0] # plus = pelaaja vasemmalla
            y_erotus = a.sijainti[1] - self.pelaaja.sijainti[1] # plus = pelaaja ylhäällä

            etaisyys_pelaajaan = math.sqrt((a.sijainti[0] - self.pelaaja.sijainti[0])**2 + (a.sijainti[1] - self.pelaaja.sijainti[1])**2)
            

            x_suhde = 0
            y_suhde = 0
            if x_erotus != 0 and y_erotus != 0:

                x_suhde = -x_erotus / (abs(x_erotus)+abs(y_erotus))
                y_suhde = -y_erotus / (abs(x_erotus)+abs(y_erotus))

            print(f"{etaisyys_pelaajaan}    {x_suhde}    {(y_suhde)}")

            x_norm = math.copysign(1,-x_erotus)
            y_norm = math.copysign(1,-y_erotus)
            
            v = 0.1

            a.vauhti = a.vauhti[0] + v*(x_suhde + (x_norm * etaisyys_pelaajaan/1000)), a.vauhti[1] + v*(y_suhde + (y_norm * etaisyys_pelaajaan/1000))
            #a.vauhti = a.vauhti[0] + x_norm/20 - x_erotus/20 , a.vauhti[1] + y_norm/20 - y_erotus/20
            
            self.tarkasta_max_vauhti(a)

            for b in self.aaveet:
                if a != b:
                    if a.sijainti[0] != b.sijainti[0]: 
                        x_erotus = a.sijainti[0] - b.sijainti[0] 
                    if a.sijainti[1] != b.sijainti[1]:
                        y_erotus = a.sijainti[1] - b.sijainti[1]
                    x_norm = math.copysign(1,x_erotus)
                    y_norm = math.copysign(1,y_erotus)     

                    a.vauhti = a.vauhti[0] + x_norm * (5/x_erotus)**2 , a.vauhti[1] + y_norm * (5/y_erotus)**2
            max_vauhti = a.max_vauhti

            if a.vauhti[0] > max_vauhti:
                a.vauhti = max_vauhti, a.vauhti[1]
            if a.vauhti[1] > max_vauhti:
                a.vauhti = a.vauhti[0], max_vauhti
            if a.vauhti[0] < -max_vauhti:
                a.vauhti = -max_vauhti, a.vauhti[1]
            if a.vauhti[1] < -max_vauhti:
                a.vauhti = a.vauhti[0], -max_vauhti
            a.sijainti = a.sijainti[0] + a.vauhti[0], a.sijainti[1] + a.vauhti[1]
            #### LASKE ETÄISYYS, EI VAIN X tai Y etä=  sqrt(x**2 +y**2)

    def tarkasta_max_vauhti(self, hahmo):
            if hahmo.vauhti[0] > hahmo.max_vauhti:
                hahmo.vauhti = hahmo.max_vauhti, hahmo.vauhti[1]
            if hahmo.vauhti[1] > hahmo.max_vauhti:
                hahmo.vauhti = hahmo.vauhti[0], hahmo.max_vauhti
            if hahmo.vauhti[0] < -hahmo.max_vauhti:
                hahmo.vauhti = -hahmo.max_vauhti, hahmo.vauhti[1]
            if hahmo.vauhti[1] < -hahmo.max_vauhti:
                hahmo.vauhti = hahmo.vauhti[0], -hahmo.max_vauhti


    def piirra_naytto(self):
        self.naytto.fill((100,100,100))
        self.naytto.blit(self.pelaaja.kuva, self.pelaaja.sijainti)
        for a in self.aaveet:
            self.naytto.blit(a.kuva, a.sijainti)
            if a.rect.colliderect(self.pelaaja.rect):
                print("moo")
            pygame.draw.rect(self.naytto,(0,0,0),a.rect,10)
        pygame.display.flip()

    def pelaa(self):

        while True:
            self.tutki_tapahtumat()
            self.liikuta_aaveita2()
            self.piirra_naytto()
        
            self.kello.tick(60)





if __name__ == "__main__":
    
    peli = Peli()
