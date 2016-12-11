import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1600, 830))
done = False
is_blue = True
s = 0
s1 = 0
x = 690
y = 450
r = 1
dead = True
dead1 = True
x1 = 30
y1 = 30
r1 = 0
p = [[0 ,0, -1, 200]]
f = True
f1 = True
p1 = [[0 ,0, -1, 200]]
ftrue = True

clock = pygame.time.Clock()

while not done:
    if not dead or not dead1:
        if dead:
            s += 1
            ftrue = True
        if dead1:
            s1 += 1
            ftrue = False
        x = 690
        y = 450
        r = 1
        dead = True
        dead1 = True
        x1 = 30
        y1 = 30
        r1 = 0
        p = [[0 ,0, -1, 200]]
        p1 = [[0 ,0, -1, 200]]
        f = True
        f1 = True
    if x<0:
        x += 1600
    elif x>1600:
        x-= 1600
    if y<0:
        y += 830
    elif y>830:
        y -=830
    if x1<0:
        x1 += 1600
    elif x1>1600:
        x1-= 1600
    if y1<0:
        y1 += 830
    elif y1>830:
        y1 -=830
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y += int(round(5*math.sin(r*math.pi)))
        x += int(round(5*math.cos(r*math.pi)))
    if pressed[pygame.K_DOWN]:
        y -= int(round(5*math.sin(r*math.pi)))
        x -= int(round(5*math.cos(r*math.pi)))
    if pressed[pygame.K_RIGHT]: r += .02
    if pressed[pygame.K_LEFT]: r -= .02
    if pressed[pygame.K_RSHIFT]:
        if len(p) < 2 and f:
            p.append([x+int(round(30*math.cos(r*math.pi))), y+int(round(30*math.sin(r*math.pi))), r, 40])
            f = False
    else: f = True

    if pressed[pygame.K_w]:
        y1 += int(round(5*math.sin(r1*math.pi)))
        x1 += int(round(5*math.cos(r1*math.pi)))
    if pressed[pygame.K_s]:
        y1 -= int(round(5*math.sin(r1*math.pi)))
        x1 -= int(round(5*math.cos(r1*math.pi)))
    if pressed[pygame.K_d]: r1 += .02
    if pressed[pygame.K_a]: r1 -= .02
    if pressed[pygame.K_q]:
        if len(p1) < 2 and f1:
            p1.append([x1+int(round(30*math.cos(r1*math.pi))), y1+int(round(30*math.sin(r1*math.pi))), r1, 40])
            f1 = False
    else: f1 = True


    if ftrue:
        screen.fill((0, 100, 200))
    else:
        screen.fill((200, 100, 0))
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myfont.render("one: "+str(s)+" two: "+str(s1), 1, (255, 0, 0))
    screen.blit(label, (320, 200))
    if dead:
        pygame.draw.circle(screen, (0, 125, 255), (x, y), 25)
        pygame.draw.circle(screen, (0,0,0), (x+int(round(30*math.cos((r-.125)*math.pi))), y+int(round(30*math.sin((r-.125)*math.pi)))), 5)
        pygame.draw.circle(screen, (0,0,0), (x+int(round(30*math.cos((r+.125)*math.pi))), y+int(round(30*math.sin((r+.125)*math.pi)))), 5)

    if dead1:
        pygame.draw.circle(screen, (255, 125, 0), (x1, y1), 25)
        pygame.draw.circle(screen, (0,0,0), (x1+int(round(30*math.cos((r1-.125)*math.pi))), y1+int(round(30*math.sin((r1-.125)*math.pi)))), 5)
        pygame.draw.circle(screen, (0,0,0), (x1+int(round(30*math.cos((r1+.125)*math.pi))), y1+int(round(30*math.sin((r1+.125)*math.pi)))), 5)



    for i in p:
        if i[0]<0:
            p.remove(i)
        elif i[0]>1600:
            p.remove(i)
        elif i[1]<0:
            p.remove(i)
        elif i[1]>830:
            p.remove(i)
        if i[3] > 0:
            i[1] += int(round(20*math.sin(i[2]*math.pi)))
            i[0] += int(round(20*math.cos(i[2]*math.pi)))
            i[3] -= 1
        pygame.draw.circle(screen, (0,0,0), (i[0], i[1]), 5)
        if 30 > math.sqrt((abs(i[0]-x)**2)+(abs(i[1]-y)**2)):
            #dead = False
            p.remove(i)
        if 30 > math.sqrt((abs(i[0]-x1)**2)+(abs(i[1]-y1)**2)):
            dead1 = False
            p.remove(i)

    for i in p1:
        if i[0]<0:
            p1.remove(i)
        elif i[0]>1600:
            p1.remove(i)
        elif i[1]<0:
            p1.remove(i)
        elif i[1]>830:
            p1.remove(i)
        if i[3] > 0:
            i[1] += int(round(20*math.sin(i[2]*math.pi)))
            i[0] += int(round(20*math.cos(i[2]*math.pi)))
            i[3] -= 1
        pygame.draw.circle(screen, (0,0,0), (i[0], i[1]), 5)
        if 30 > math.sqrt((abs(i[0]-x)**2)+(abs(i[1]-y)**2)):
            dead = False
            p1.remove(i)
        if 30 > math.sqrt((abs(i[0]-x1)**2)+(abs(i[1]-y1)**2)):
            #dead1 = False
            p1.remove(i)

    pygame.display.flip()
    clock.tick(60)
