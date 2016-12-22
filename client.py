# Echo client program
import socket
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1600, 830))
done = False
is_blue = True
s = 0
s1 = 0
x = 200
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

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y += int(round(5*math.sin(r*math.pi)))
            x += int(round(5*math.cos(r*math.pi)))
        if pressed[pygame.K_DOWN]:
            y -= int(round(5*math.sin(r*math.pi)))
            x -= int(round(5*math.cos(r*math.pi)))
        if pressed[pygame.K_RIGHT]: r += .02
        if pressed[pygame.K_LEFT]: r -= .02
        s.sendall((x).to_bytes(2, byteorder='big'))
        data = s.recv(1024)
        print("'Received', repr(data)")
        clock.tick(60)
