import pygame as pyg
pyg.init()
import random
import os



window = pyg.display.set_mode((1050,600))

pyg.display.set_caption("DODGE BALL")
window.fill((255,255,255))

font = pyg.font.Font('freesansbold.ttf', 70)
font2 = pyg.font.Font('freesansbold.ttf', 25)
endtext =font.render("GAME OVER",True,(0,0,0))

#ball
radius=25
speed=50
spawn=20
current_spawn=0
alive_spawn=0
x=[0]*spawn
y=[0]*spawn
deadball=0
interval = 0
for k in range (0,spawn):
    x[k]=1050
    y[k]=(random.randint(50,575)//50)*50

#player
playerh=50
playerw=100
px=0
py=25
pspeed=50

#health
score=0
hx=0
hy=0
healthh=25
healthw=1050

#score
sx=0
sy=575
scoreh=25
scorew=1050

run = True
while run:
    pyg.time.delay(100)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
    window.fill((255,255,255))
    if (healthw==0):
        cscore=font.render("SCORE : "+str(score),True,(0,0,0))
        window.blit(endtext, (325,100))
        window.blit(cscore, (325,300))
    else:
        keys = pyg.key.get_pressed()
        pyg.draw.rect(window,(50,50,50),(0,25,50,550))
        pyg.draw.rect(window,(0,255,0),(hx,hy,healthw,healthh))
        if keys[pyg.K_UP]:
            if py - pspeed > 0 :
                py -= pspeed
        if keys[pyg.K_DOWN]:
            if py+pspeed+playerh < 600:
                py += pspeed
        pyg.draw.rect(window,(0,0,255),(px,py,playerw,playerh))
        hbar=font2.render("HP : "+str(healthw//210),True,(0,0,0))
        window.blit(hbar, (0,0))
        pyg.draw.rect(window,(100,100,0),(sx,sy,scorew,scoreh))
        cscore=font2.render("SCORE : "+str(score),True,(0,0,0))
        window.blit(cscore, (0,575))
        if (((pyg.time.get_ticks()/1000)-interval>=0.25) and (current_spawn<spawn)):
            current_spawn+=1
            interval+=0.25
        if deadball==1:
            for j in range (0,spawn-1):
                y[j]=y[j+1]
                x[j]=x[j+1]
            y[9]=(random.randint(50,575)//50)*50
            x[9]=1050
            current_spawn-=1
            deadball=0
        for k in range (alive_spawn,current_spawn):
            if x[k]-radius-speed>=50 :
                x[k]-=speed
                pyg.draw.circle(window,(255,0,0),(x[k],y[k]),radius)
            else :
                if py<y[k]<(py+50):
                    pyg.draw.rect(window,(255,100,0),((px-50),py,50,playerh))
                    healthw-=210
                else:
                    score+=1
                deadball=1
    pyg.display.update()
     
pyg.quit()

os.system("library.py")