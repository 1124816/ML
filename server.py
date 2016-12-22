# Echo server program
import socket
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

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(4096)
            print(data)
            s.sendall(data)
            if not data: break
            screen.fill((200, 100, 0))
            pygame.draw.circle(screen, (0, 125, 255), (int.from_bytes(data, byteorder='big'), 200), 25)
            pygame.display.flip()
            clock.tick(60)
