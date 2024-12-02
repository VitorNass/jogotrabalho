import pygame
import random

from pygame.freetype import SysFont

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo em python')


bg = pygame.image.load('asset/City2_pale.png').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))
bg = pygame.transform.rotate(bg, 360)

alien = pygame.image.load('asset/Player1.png').convert_alpha()
alien1 = pygame.image.load('asset/Player1.png').convert_alpha()
alien2 = pygame.image.load('asset/Player1.png').convert_alpha()
alien = pygame.transform.scale(alien, (109,69))
alien1 = pygame.transform.scale(alien1, (109,69))
alien2 = pygame.transform.scale(alien2, (109,69))

playerImg = pygame.image.load('asset/Enemy1.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (86,39)) #conversão do tamanho da nave
playerImg = pygame.transform.rotate(playerImg, 360)

missil = pygame.image.load('asset/Enemy1Shot.png').convert_alpha()
missil = pygame.transform.scale(missil, (86,39)) #conversão do tamanho da nave
missil= pygame.transform.rotate(missil, 360)

#controle de posições GERAL
pos_alien_x= 500
pos_alien_y= 660

pos_alien1_x= 400
pos_alien1_y= 600

pos_alien2_x= 450
pos_alien2_y= 500

pos_player_x= 200
pos_player_y= 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

pontos = 10

triggered = False
rodando = True

#transformando imagem em objeto
player_rect  = playerImg.get_rect()
alien_rect  = alien.get_rect()
alien1_rect  = alien1.get_rect()
alien2_rect  = alien2.get_rect()
missil_rect  = missil.get_rect()


#funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]
def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]
def colisions():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -=1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos +=1
        return True
    elif player_rect.colliderect(alien1_rect) or alien1_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(alien1_rect):
        pontos += 1
        return True
    elif player_rect.colliderect(alien2_rect) or alien2_rect.x == 60:
        pontos -= 1
        return True
    elif missil_rect.colliderect(alien2_rect):
        pontos += 1
        return True
    else:
        return False

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))
    rel_x= x % bg.get_rect().width
    screen.blit(bg,(rel_x - bg.get_rect().width,0))#cria backgroud
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    #posição rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.y = pos_missil_y
    missil_rect.x = pos_missil_x

    alien2_rect.y = pos_alien2_y
    alien2_rect.x = pos_alien2_x

    alien1_rect.y = pos_alien1_y
    alien1_rect.x = pos_alien1_x

    alien_rect.y = pos_alien_y
    alien_rect.x = pos_alien_x

    # controla velocidade de movimento da tela
    x-=2
    pos_alien_x -=2
    pos_alien1_x -=2.5
    pos_alien2_x -= 1.7
    pos_missil_x += vel_missil_x

    pygame.draw.rect(screen, (0, 0, 0), player_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), missil_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), alien_rect, 1)

    #criar imagens
    screen.blit(alien,(pos_alien_x, pos_alien_y))
    screen.blit(alien1, (pos_alien1_x, pos_alien1_y))
    screen.blit(alien2, (pos_alien2_x, pos_alien2_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))
    pygame.display.update()

    print(pontos)

    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -=1
        if not triggered:
            pos_missil_y -=1

    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y +=1
        if not triggered:
            pos_missil_y +=1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 5
    #respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()
    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    if pos_alien1_x == 30:
        pos_alien1_x = respawn()[0]
        pos_alien1_y = respawn()[1]
    if pos_alien1_x == 30 or colisions():
        pos_alien1_x = respawn()[0]
        pos_alien1_y = respawn()[1]
    if pos_alien2_x == 70 :
        pos_alien2_x = respawn()[0]
        pos_alien2_y = respawn()[1]
    if pos_alien2_x == 70 or colisions():
        pos_alien2_x = respawn()[0]
        pos_alien2_y = respawn()[1]