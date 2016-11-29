import pygame
import math

pygame.init()
screen = pygame.display.set_mode((720, 480))
done = False
is_blue = True
x = 30
y = 30
r = 0

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y += int(round(3*math.sin(r*math.pi)))
            x += int(round(3*math.cos(r*math.pi)))
        if pressed[pygame.K_DOWN]:
            y -= int(round(3*math.sin(r*math.pi)))
            x -= int(round(3*math.cos(r*math.pi)))
        if pressed[pygame.K_w]: r += .01
        if pressed[pygame.K_q]: r -= .01

        screen.fill((255, 255, 255))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.circle(screen, color, (x, y), 25)
        pygame.draw.circle(screen, (0,0,0), (x+int(round(30*math.cos((r-.125)*math.pi))), y+int(round(30*math.sin((r-.125)*math.pi)))), 5)
        pygame.draw.circle(screen, (0,0,0), (x+int(round(30*math.cos((r+.125)*math.pi))), y+int(round(30*math.sin((r+.125)*math.pi)))), 5)

        pygame.display.flip()
        clock.tick(60)
