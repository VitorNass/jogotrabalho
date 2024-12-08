import pygame
import random
import os
import sys

def resource_path(relative_path):
    try:
        # Caminho quando executado como um .exe
        base_path = sys._MEIPASS
    except AttributeError:
        # Caminho durante o desenvolvimento
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

from pygame.freetype import SysFont

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Meu jogo em python')

bg = pygame.image.load(resource_path('asset/City2_pale.png')).convert_alpha()
bg = pygame.transform.scale(bg, (x, y))
bg = pygame.transform.rotate(bg, 360)

enemies = pygame.image.load(resource_path('asset/Player1.png')).convert_alpha()
enemies1 = pygame.image.load(resource_path('asset/Player2.png')).convert_alpha()
enemies2 = pygame.image.load(resource_path('asset/Player2.png')).convert_alpha()
enemies = pygame.transform.scale(enemies, (109, 69))
enemies1 = pygame.transform.scale(enemies1, (109, 69))
enemies2 = pygame.transform.scale(enemies2, (109, 69))

playerImg = pygame.image.load(resource_path('asset/TopDownCar.png')).convert_alpha()
playerImg = pygame.transform.scale(playerImg, (86, 39))  # conversão do tamanho da nave
playerImg = pygame.transform.rotate(playerImg, 360)

missil = pygame.image.load(resource_path('asset/Enemy1Shot.png')).convert_alpha()
missil = pygame.transform.scale(missil, (86, 39))  # conversão do tamanho da nave
missil = pygame.transform.rotate(missil, 360)

# controle de posições GERAL
pos_enemies_x = 500
pos_enemies_y = 660

pos_enemies1_x = 400
pos_enemies1_y = 600

pos_enemies2_x = 450
pos_enemies2_y = 500

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

pontos = 10

triggered = False
rodando = True

# transformando imagem em objeto
player_rect = playerImg.get_rect()
enemies_rect = enemies.get_rect()
enemies1_rect = enemies1.get_rect()
enemies2_rect = enemies2.get_rect()
missil_rect = missil.get_rect()


# funções
def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]


def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]


def colisions():
    global pontos
    if player_rect.colliderect(enemies_rect) or enemies_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(enemies_rect):
        pontos += 1
        return True
    elif player_rect.colliderect(enemies1_rect) or enemies1_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(enemies1_rect):
        pontos += 1
        return True
    elif player_rect.colliderect(enemies2_rect) or enemies2_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(enemies2_rect):
        pontos += 1
        return True
    else:
        return False


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0, 0))
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))  # cria background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    # posição rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.y = pos_missil_y
    missil_rect.x = pos_missil_x

    enemies2_rect.y = pos_enemies2_y
    enemies2_rect.x = pos_enemies2_x

    enemies1_rect.y = pos_enemies1_y
    enemies1_rect.x = pos_enemies1_x

    enemies_rect.y = pos_enemies_y
    enemies_rect.x = pos_enemies_x

    # controla velocidade de movimento da tela
    x -= 2
    pos_enemies_x -= 2
    pos_enemies1_x -= 2.5
    pos_enemies2_x -= 1.7
    pos_missil_x += vel_missil_x

    pygame.draw.rect(screen, (0, 0, 0), player_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), missil_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), enemies_rect, 1)

    # criar imagens
    screen.blit(enemies, (pos_enemies_x, pos_enemies_y))
    screen.blit(enemies1, (pos_enemies1_x, pos_enemies1_y))
    screen.blit(enemies2, (pos_enemies2_x, pos_enemies2_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))
    pygame.display.update()

    print(pontos)

    # teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 1
        if not triggered:
            pos_missil_y -= 1

    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 1
        if not triggered:
            pos_missil_y += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 5
    # respawn
    if pos_enemies_x == 50:
        pos_enemies_x = respawn()[0]
        pos_enemies_y = respawn()[1]
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()
    if pos_enemies_x == 50 or colisions():
        pos_enemies_x = respawn()[0]
        pos_enemies_y = respawn()[1]
    if pos_enemies1_x == 30:
        pos_enemies1_x = respawn()[0]
        pos_enemies1_y = respawn()[1]
    if pos_enemies1_x == 30 or colisions():
        pos_enemies1_x = respawn()[0]
        pos_enemies1_y = respawn()[1]
    if pos_enemies2_x == 70:
        pos_enemies2_x = respawn()[0]
        pos_enemies2_y = respawn()[1]
    if pos_enemies2_x == 70 or colisions():
        pos_enemies2_x = respawn()[0]
        pos_enemies2_y = respawn()[1]
